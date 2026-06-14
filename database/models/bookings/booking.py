from django.db import models

class Booking(models.Model):
    """
    Model representing a customer taxi booking request.
    """
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'bookings'
        db_table = 'bookings_booking'
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self) -> str:
        return str(self.name)
