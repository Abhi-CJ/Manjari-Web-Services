from django.test import TestCase
from bookings.forms import BookingForm
from core.models import Service
from core.constants import DEFAULT_SERVICE_CHOICES

class BookingFormTests(TestCase):
    """
    Test suite for BookingForm choice validation and dynamic loading.
    """
    def test_form_uses_fallback_choices_when_database_empty(self) -> None:
        # Clear any existing services
        Service.objects.all().delete()
        
        form = BookingForm()
        field_choices = form.fields['service_type'].choices
        
        # Expected is default list + empty option
        expected_choices = [('', 'Select service type')] + DEFAULT_SERVICE_CHOICES
        self.assertEqual(list(field_choices), expected_choices)

    def test_form_loads_service_choices_from_database(self) -> None:
        # Clear and create specific service
        Service.objects.all().delete()
        Service.objects.create(title="VVIP Escort", description="Secure luxury transit")
        
        form = BookingForm()
        field_choices = form.fields['service_type'].choices
        
        self.assertIn(('VVIP Escort', 'VVIP Escort'), field_choices)
        self.assertEqual(len(field_choices), 2)  # Empty option + VVIP Escort
