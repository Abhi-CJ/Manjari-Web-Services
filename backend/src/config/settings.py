# -------------------------------
# ALLOWED HOSTS
# -------------------------------
hosts = [
    host.strip()
    for host in CONFIG(
        'ALLOWED_HOSTS',
        default='localhost,127.0.0.1'
    ).split(',')
    if host.strip()
]

for host in ['localhost', '127.0.0.1', 'testserver', '0.0.0.0''manjari-web-services-production.up.railway.app']:
    if host not in hosts:
        hosts.append(host)

ALLOWED_HOSTS = hosts


# -------------------------------
# CSRF TRUSTED ORIGINS
# Add your Railway/custom domain later
# -------------------------------
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://localhost',
    'https://127.0.0.1',
    
    'https://manjari-web-services-production.up.railway.app',
]


# -------------------------------
# STATIC FILES
# -------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'src',
    BASE_DIR / 'frontend' / 'assets',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'frontend' / 'assets' / 'media'


# Django 6 + WhiteNoise
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# -------------------------------
# SECURITY SETTINGS
# -------------------------------
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_SSL_REDIRECT = True

    SECURE_PROXY_SSL_HEADER = (
        'HTTP_X_FORWARDED_PROTO',
        'https',
    )

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

else:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
