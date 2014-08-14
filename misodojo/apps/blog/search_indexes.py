# -*-*- encoding: utf-8 -*-*-
from django.utils import timezone
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # use timezone.now instead of native datetime to avoid errors like:
        # RuntimeWarning: DateTimeField received a naive datetime
        return self.get_model().objects.filter(created__lte=timezone.now())
