from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
from core.models import Service
from bookings.models import Booking

class BookingViewTests(TestCase):
    """
    Test suite for booking views and rate limiting controllers.
    """
    def setUp(self) -> None:
        cache.clear()
        Service.objects.create(title="Airport Transfer", description="Taxi to/from airport")
        self.booking_url = reverse("submit_booking")
        self.booking_data = {
            "name": "John Doe",
            "phone": "9399623699",
            "pickup_location": "Gwalior Airport",
            "drop_location": "Sada, Gwalior",
            "service_type": "Airport Transfer",
            "message": "Need a clean car please."
        }

    def test_booking_invalid_data_does_not_create_booking(self) -> None:
        invalid_data = self.booking_data.copy()
        invalid_data["name"] = ""  # required field is blank
        
        response = self.client.post(self.booking_url, invalid_data)
        
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Booking.objects.count(), 0)

    def test_booking_rate_limit(self) -> None:
        # We allow up to 3 bookings in 5 minutes. Make 3 successful bookings.
        for i in range(3):
            data = self.booking_data.copy()
            data["name"] = f"User {i}"
            response = self.client.post(self.booking_url, data)
            self.assertRedirects(response, reverse("home"))
            
        # The 4th booking from the same client IP should be rate limited.
        data = self.booking_data.copy()
        data["name"] = "User 4"
        response = self.client.post(self.booking_url, data)
        self.assertRedirects(response, reverse("home"))
        
        # Verify only 3 bookings exist in the database
        self.assertEqual(Booking.objects.count(), 3)
