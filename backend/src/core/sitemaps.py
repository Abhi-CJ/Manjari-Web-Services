# core/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import RoutePage


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class RoutePageSitemap(Sitemap):
    """Sitemap for dynamically created SEO route/landing pages."""

    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return RoutePage.objects.filter(is_published=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated_at