from django.views.generic import DetailView, ListView
from .models import *


class BlogView(ListView):
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
        return context

    def render_to_response(self, context):
        if self.request.is_ajax():
            self.template_name = 'blog/posts.html'
        return ListView.render_to_response(self, context)


class PostView(DetailView):
    """Blog post view"""
    http_method_names = ['get']
    template_name = 'blog/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        return context
