# -*-*- encoding: utf-8 -*-*-
# pylint: disable=E1101,R0901
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from haystack.forms import SearchForm
# from core.mixins import CachinMixin  # Using Cloudflare for caching
from .models import Post


class BlogView(ListView):  # was: CachinMixin, ListView
    """Blog index view"""
    model = Post
    paginate_by = 5
    http_method_names = ['get']
    template_name = 'blog/index.html'

    def get_queryset(self):
        m = Post.objects.select_related().filter(published=True)
        if 'slug' in self.kwargs:  # we need to filter on the tag
            m = m.filter(tags__slug__in=[self.kwargs['slug']])
        if self.request.is_ajax():
            try:
                offset = int(self.request.REQUEST.get('offset'))
            except:
                offset = 0
            if offset:
                m = m[offset:offset + BlogView.paginate_by]
        return m

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        if not self.request.is_ajax():
            context['ranking'] = Post.ranking()
        context['topic'] = self.kwargs.get('slug', '')
        context['form'] = SearchForm()
        return context

    def render_to_response(self, context):
        if self.request.is_ajax():
            self.template_name = 'blog/posts.html'
        return ListView.render_to_response(self, context)


class PostView(DetailView):  # was: CachinMixin, DetailView
    """Blog post view"""
    http_method_names = ['get']
    template_name = 'blog/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        return context


class RssSiteFeed(Feed):
    """Support for feeds."""
    title = "infinite sushi"
    link = "/feed/"
    description = "Latest posts."

    def items(self):
        return Post.objects.select_related().filter(published=True).order_by('-created')[:5]

    def item_description(self, item):
        return item.summary

class AtomEntryCustomFeed(Atom1Feed):
    """Atom feed with content element."""
    def add_item_elements(self, handler, item):
        super(AtomEntryCustomFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u"content", item['content'])


class AtomSiteFeed(RssSiteFeed):
    feed_type = AtomEntryCustomFeed
    subtitle = RssSiteFeed.description

    def item_extra_kwargs(self, item):
        """Add the 'content' field of the 'Entry' item, to be used by the custom feed generator."""
        return {'content': item.content}
