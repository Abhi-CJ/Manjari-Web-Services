from typing import List, Tuple

# Rate Limiting Configurations
DEFAULT_RATE_LIMIT_COUNT: int = 3
DEFAULT_RATE_LIMIT_PERIOD: int = 300  # 5 minutes in seconds

REVIEW_RATE_LIMIT_PREFIX: str = "submit_review"
BOOKING_RATE_LIMIT_PREFIX: str = "create_booking"

# Review Constants
DEFAULT_REVIEW_RATING: int = 5
MAX_REVIEW_RATING: int = 5
MIN_REVIEW_RATING: int = 1

# Booking Choice Fallbacks
DEFAULT_SERVICE_CHOICES: List[Tuple[str, str]] = [
    ('Local Cab', 'Local Cab'),
    ('Airport Taxi', 'Airport Taxi'),
    ('Outstation Trip', 'Outstation Trip'),
    ('Wedding Cab', 'Wedding Cab'),
]
