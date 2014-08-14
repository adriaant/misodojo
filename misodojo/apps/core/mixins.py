# -*-*- encoding: utf-8 -*-*-
import hashlib
from django.conf import settings
from django.core.cache import cache
from django.utils.cache import patch_response_headers, get_max_age
from django.utils.encoding import iri_to_uri, force_bytes


class CachinMixin(object):
    """
       This is a mixin to cache responses on a per view basis, without
       having to use decorators and allowing for custom changes. It is
       also simpler than the django caching system.
       The mixin knows the difference between web requests and ajax requests
       and will cache appopriately.
    """

    def dispatch(self, request, *args, **kwargs):
        # We only cache GET requests and we don't cache for our masters
        if request.method != 'GET' or request.user.is_authenticated():
            return super(CachinMixin, self).dispatch(request, *args, **kwargs)

        # Check whether the response data is in the cache.
        key = self.get_cache_key(request)
        response = cache.get(key) or None
        if response is not None:
            return response

        response = super(CachinMixin, self).dispatch(request, *args, **kwargs)
        # Only cache on OK resposne
        if response.status_code == 200:
            self.cache_response(key, response)
        return response

    def get_cache_key(self, request):
        '''We use the path, query and one header, that is enough for our purposes'''
        querystring = request.META.get('QUERY_STRING', '')  # important for paging and the like
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH', '')  # tells us if it's an ajax request
        val = ':'.join([settings.CACHE_MIDDLEWARE_KEY_PREFIX, request.path, is_ajax, querystring])
        key = hashlib.md5(force_bytes(iri_to_uri(val)))
        return key.hexdigest()

    def cache_response(self, key, response):
        '''Code below is very nearly the same as in django's cache middleware'''
        timeout = get_max_age(response)
        if timeout is None:
            timeout = settings.CACHE_MIDDLEWARE_SECONDS
        patch_response_headers(response, timeout)
        if hasattr(response, 'render') and callable(response.render):
            response.add_post_render_callback(
                lambda r: cache.set(key, r, timeout)
            )
        else:
            cache.set(key, response, timeout)
        return response
