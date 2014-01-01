from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

 
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.CharField(max_length=255, null=True, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']
 
    def __unicode__(self):
        return self.title
 
    def get_absolute_url(self):
        return reverse('blog_post', args=[self.slug])
