from django.core.cache import cache
from django.contrib import messages
from django.http import HttpRequest
from .ip import get_client_ip
from core.constants import DEFAULT_RATE_LIMIT_COUNT, DEFAULT_RATE_LIMIT_PERIOD

def is_rate_limited(
    request: HttpRequest,
    key_prefix: str,
    limit: int = DEFAULT_RATE_LIMIT_COUNT,
    period: int = DEFAULT_RATE_LIMIT_PERIOD,
    error_message: str = "Too many requests. Please try again later."
) -> bool:
    """
    Checks if the client IP has exceeded the rate limit.
    If limited, adds a Django error message and returns True.
    Otherwise, increments the counter and returns False.
    """
    ip = get_client_ip(request)
    cache_key = f"rate_limit_{key_prefix}_{ip}"
    request_count = cache.get(cache_key, 0)

    if request_count >= limit:
        messages.error(request, error_message)
        return True

    # Increment counter and set/update cache with timeout
    cache.set(cache_key, request_count + 1, period)
    return False
