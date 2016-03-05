from django import template
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def pages_list(curpath):
    """Grabs the flatpages and lists them for inclusion in the bootstrap navbar."""
    fp = FlatPage.objects.all().values_list('title', 'url')
    h = u''
    for t, u in fp:
        h += u'<li'
        if u in curpath:
            h += u' class="active"'
        h += u'><a href="'
        h += reverse('django.contrib.flatpages.views.flatpage', kwargs={'url': u})
        h += u'">' + t + u'</a></li>'
    return mark_safe(h)
