from django.conf.urls import (patterns, url)
from .views import *

urlpatterns = patterns('',
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
