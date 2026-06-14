from django.test import TestCase
from django.core import mail
from django.core.cache import cache
from core.models import Service
from bookings.models import Booking
from bookings.services import BookingService
from bookings.types import BookingFormData

class BookingServiceTests(TestCase):
    """
    Test suite for BookingService business logic and email notifications.
    """
    def setUp(self) -> None:
        cache.clear()
        Service.objects.create(title="Airport Transfer", description="Taxi to/from airport")
        self.booking_data: BookingFormData = {
            "name": "John Doe",
            "phone": "9399623699",
            "pickup_location": "Gwalior Airport",
            "drop_location": "Sada, Gwalior",
            "service_type": "Airport Transfer",
            "message": "Need a clean car please."
        }

    def test_booking_service_creation_sends_email(self) -> None:
        self.assertEqual(len(mail.outbox), 0)
        
        booking = BookingService.create_booking(self.booking_data)
        
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(booking.name, "John Doe")
        
        # Verify notification email was sent
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertIn("New Taxi Booking Request - John Doe", sent_email.subject)
        self.assertIn("Gwalior Airport", sent_email.body)
        self.assertIn("Sada, Gwalior", sent_email.body)
