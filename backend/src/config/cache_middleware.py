"""
Cache-Control headers middleware for optimized content delivery
"""
from django.utils.cache import patch_response_headers
from django.http import HttpResponse


class CacheHeadersMiddleware:
    """
    Adds appropriate Cache-Control headers based on content type.
    - Static assets (CSS, JS, images): 1 year immutable
    - Pages: 1 hour
    - Media: 24 hours private
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Static assets - cache for 1 year (immutable)
        if self._is_static_asset(request.path):
            patch_response_headers(response, cache_timeout=31536000)
            response['Cache-Control'] = 'public, max-age=31536000, immutable'
        
        # Media files - cache for 24 hours
        elif request.path.startswith('/media/'):
            patch_response_headers(response, cache_timeout=86400)
            response['Cache-Control'] = 'private, max-age=86400'
        
        # HTML pages - cache for 1 hour
        elif response.get('Content-Type', '').startswith('text/html'):
            patch_response_headers(response, cache_timeout=3600)
            response['Cache-Control'] = 'public, max-age=3600'
        
        return response
    
    @staticmethod
    def _is_static_asset(path):
        """Check if path is a static asset (CSS, JS, images, fonts)."""
        static_extensions = ('.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.woff', '.woff2', '.ttf', '.eot')
        return any(path.endswith(ext) for ext in static_extensions)
