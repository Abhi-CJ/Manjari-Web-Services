"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/deployment/asgi/
"""

import os
import sys
from pathlib import Path

# Prepend src directory to Python's path so config, core, and bookings can be resolved
base_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(base_dir / 'src'))

# Prepend project root so 'database' can be imported
sys.path.insert(0, str(base_dir.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.asgi import get_asgi_application
application = get_asgi_application()
