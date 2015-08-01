# -*-*- encoding: utf-8 -*-*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.cache import cache
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class AutoDateTimeField(models.DateTimeField):
    '''An editable version of created date field, without the hassle
       of overriding save() in the actual models.'''
    def pre_save(self, model_instance, add):
        if not add:
            return getattr(model_instance, self.attname)
        now = timezone.now()
        setattr(model_instance, self.attname, now)
        return now

    def deconstruct(self):
        """ Support Django 1.7+ migrations """
        return super(
            AutoDateTimeField, self).deconstruct()


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.CharField(max_length=255, null=True, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = AutoDateTimeField(null=False, blank=True)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', args=[self.slug])

    @classmethod
    def ranking(cls):
        cache_key = 'tag_ranking'
        ranking_list = cache.get(cache_key) or None
        if ranking_list is None:
            l = list(Post.tags.most_common()[:20])
            ranking_list = sorted(l, key=lambda x: (-x.num_times, x.name))
            cache.set(cache_key, ranking_list, 3600)
        return ranking_list
