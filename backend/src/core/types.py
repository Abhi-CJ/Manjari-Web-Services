from typing import TypedDict

class ReviewFormData(TypedDict):
    customer_name: str
    location: str
    rating: int
    review: str
