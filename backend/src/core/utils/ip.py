from django.http import HttpRequest

def get_client_ip(request: HttpRequest) -> str:
    """
    Extract client IP address from request headers or remote address.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR') or '127.0.0.1'
    return ip
