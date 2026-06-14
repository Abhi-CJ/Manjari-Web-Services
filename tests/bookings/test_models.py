from django.test import TestCase
from bookings.models import Booking

class BookingModelTests(TestCase):
    """
    Test suite for Booking model.
    """
    def test_booking_string_representation(self) -> None:
        booking = Booking.objects.create(
            name="Alice Smith",
            phone="9876543210",
            pickup_location="Station",
            drop_location="Hotel",
            service_type="Local Cab"
        )
        self.assertEqual(str(booking), "Alice Smith")
