from django.conf.urls import (patterns, url)
from haystack.forms import SearchForm
from haystack.views import SearchView, search_view_factory
from .views import *

urlpatterns = patterns('haystack.views',
    url(r'^search/$', search_view_factory(
        view_class=SearchView, form_class=SearchForm),
        name='haystack_search'),
)

urlpatterns += patterns('',
    url(
        regex=r"^$",
        view=BlogView.as_view(),
        name="blog_index"
    ),
    url(
        regex=r'^topics/(?P<slug>[\w\-]+)/$',
        view=BlogView.as_view(),
        name="blog_topic"
    ),
    url(
        regex=r'^(?P<slug>[\w\-]+)/$',
        view=PostView.as_view(),
        name="blog_post"
    ),
)
