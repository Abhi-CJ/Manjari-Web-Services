from django.conf import settings
from django.http import HttpRequest
from typing import Dict, Any

def contact_info(request: HttpRequest) -> Dict[str, Any]:
    """
    Context processor to inject dynamic contact settings to all templates.
    """
    return {
        'CONTACT_PHONE': getattr(settings, 'CONTACT_PHONE', '+919399623699'),
        'CONTACT_PHONE_DISPLAY': getattr(settings, 'CONTACT_PHONE_DISPLAY', '+91 9399623699'),
        'CONTACT_EMAIL': getattr(settings, 'CONTACT_EMAIL', 'info@manjaritaxi.com'),
        'WHATSAPP_LINK': getattr(settings, 'WHATSAPP_LINK', 'https://wa.me/919399623699'),
    }
