from django import template
from core.models import RoutePage

register = template.Library()

@register.simple_tag
def get_route_pages(limit=6):
    """
    Returns a list of published route pages for the footer navigation.
    Limits to the most recently updated or by a specific logic.
    """
    return RoutePage.objects.filter(is_published=True).order_by('title')[:limit]

@register.filter(name='sanitize')
def sanitize(value):
    """
    Sanitizes HTML content to prevent XSS.
    """
    import bleach
    allowed_tags = [
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
        'em', 'i', 'li', 'ol', 'strong', 'ul', 'p', 'br',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'span',
        'table', 'tbody', 'td', 'th', 'thead', 'tr'
    ]
    allowed_attributes = {
        'a': ['href', 'title', 'target'],
        'abbr': ['title'],
        'acronym': ['title'],
        '*': ['class', 'id']
    }
    return bleach.clean(
        value,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )
