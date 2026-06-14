from core.models import Review
from core.types import ReviewFormData

class ReviewService:
    """
    Service layer class containing business logic for Reviews.
    """
    @staticmethod
    def create_review(data: ReviewFormData) -> Review:
        """
        Creates a new Review instance and saves it to the database.
        By default, all reviews are set to approved=False.
        """
        review = Review(
            customer_name=data['customer_name'],
            location=data['location'],
            rating=data['rating'],
            review=data['review'],
            approved=False
        )
        review.save()
        return review
