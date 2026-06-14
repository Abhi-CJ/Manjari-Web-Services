from django.test import TestCase
from core.models import Service, Vehicle, Review

class CoreModelTests(TestCase):
    """
    Test suite for core models Service, Vehicle, and Review.
    """
    def setUp(self) -> None:
        self.service = Service.objects.create(
            title="Outstation Trip",
            description="Comfortable rides out of town"
        )
        self.vehicle = Vehicle.objects.create(
            name="Maruti Dzire",
            category="Sedan",
            image="vehicles/dzire.jpg",
            seats=4,
            features=["AC", "Luggage Space", "Music System"]
        )
        self.review = Review.objects.create(
            customer_name="Jane Doe",
            location="Gwalior",
            review="Amazing service!",
            rating=5,
            approved=False
        )

    def test_service_string_representation(self) -> None:
        self.assertEqual(str(self.service), "Outstation Trip")

    def test_vehicle_string_representation(self) -> None:
        self.assertEqual(str(self.vehicle), "Maruti Dzire")

    def test_review_string_representation(self) -> None:
        self.assertEqual(str(self.review), "Jane Doe")
        self.assertFalse(self.review.approved)
