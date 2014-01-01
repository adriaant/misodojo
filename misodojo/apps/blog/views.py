from django.views.generic import DetailView, ListView, TemplateView
from .models import *


class BlogView(ListView):
    """Blog index view"""
    model = Post
    paginate_by = 20
    http_method_names = ['get']
    template_name = 'blog/index.html'

    def get_queryset(self):
         return Post.objects.select_related().filter(published=True)


class PostView(DetailView):
    """Blog post view"""
    http_method_names = ['get']
    template_name = 'blog/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        print context
        return context
