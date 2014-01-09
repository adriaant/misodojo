from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class AutoDateTimeField(models.DateTimeField):
    '''An editable version of created date field, without the hassle
       of overriding save() in the actual models.'''
    def pre_save(self, model_instance, add):
        if not add:
            return getattr(model_instance, self.attname)
        now = datetime.now()
        setattr(model_instance, self.attname, now)
        return now


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
        return list(Post.tags.most_common()[:20])


# http://south.readthedocs.org/en/latest/customfields.html#extending-introspection
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^blog\.models\.AutoDateTimeField"])
