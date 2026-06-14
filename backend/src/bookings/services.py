import threading
from django.core.mail import send_mail
from django.conf import settings
from bookings.models import Booking
from bookings.types import BookingFormData

class BookingService:
    """
    Service layer class containing business logic for Bookings.
    """
    
    @staticmethod
    def _send_notification_email(subject: str, message: str, from_email: str) -> None:
        """Helper method to send the email (designed to be run in a background thread)"""
        try:
            admin_email = getattr(settings, 'ADMIN_NOTIFICATION_EMAIL', from_email)
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=[admin_email],
                fail_silently=False,
            )
        except Exception:
            # Silent fallback on SMTP error
            pass

    @staticmethod
    def create_booking(data: BookingFormData) -> Booking:
        """
        Creates and saves a Booking record, then sends a notification email to the owner.
        SMTP exceptions are handled gracefully to prevent booking creation failures.
        """
        booking = Booking.objects.create(
            name=data['name'],
            phone=data['phone'],
            pickup_location=data['pickup_location'],
            drop_location=data['drop_location'],
            service_type=data['service_type'],
            message=data.get('message', '')
        )

        # Dispatch email notification
        subject = f"New Taxi Booking Request - {booking.name}"
        message = (
            f"You have received a new taxi booking request.\n\n"
            f"Details:\n"
            f"Name: {booking.name}\n"
            f"Phone: {booking.phone}\n"
            f"Pickup Location: {booking.pickup_location}\n"
            f"Drop Location: {booking.drop_location}\n"
            f"Service Type: {booking.service_type}\n"
            f"Message: {booking.message or 'N/A'}\n\n"
            f"Please contact the customer to confirm the booking."
        )

        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
        if from_email:
            # Send asynchronously in a background thread so the user doesn't wait for Gmail SMTP
            # Run synchronously in tests to avoid race conditions and ensure outbox captures it
            import sys
            if 'test' in sys.argv:
                BookingService._send_notification_email(subject, message, from_email)
            else:
                email_thread = threading.Thread(
                    target=BookingService._send_notification_email,
                    args=(subject, message, from_email)
                )
                email_thread.start()

        return booking
