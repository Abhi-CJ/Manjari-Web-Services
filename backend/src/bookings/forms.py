from django import forms
from django.forms import ModelForm
from bookings.models import Booking
from core.models import Service
from core.constants import DEFAULT_SERVICE_CHOICES

class BookingForm(ModelForm):
    """
    Form for creating a Booking request.
    Includes custom widgets with accessibility support.
    """
    class Meta:
        model = Booking
        fields = [
            "name",
            "phone",
            "pickup_location",
            "drop_location",
            "service_type",
            "message"
        ]
        
        labels = {
            'name': 'Your Name',
            'phone': 'Phone Number',
            'pickup_location': 'Pickup Location',
            'drop_location': 'Drop Location',
            'service_type': 'Service Type',
            'message': 'Special Requests (Optional)'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Enter your full name',
                'aria-label': 'Enter your full name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-field',
                'type': 'tel',
                'placeholder': 'e.g., +91 9399623699',
                'aria-label': 'Enter your phone number',
                'required': True
            }),
            'pickup_location': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Where should we pick you up?',
                'aria-label': 'Enter pickup location',
                'required': True
            }),
            'drop_location': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Where do you want to go?',
                'aria-label': 'Enter drop location',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-field',
                'placeholder': 'Any special requests? (e.g., luggage space, wheelchair access)',
                'aria-label': 'Enter any special requests',
                'rows': 3
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically load service types from database, fallback to defaults if database is not ready
        try:
            services = Service.objects.all().only('title')
            choices = [(service.title, service.title) for service in services]
        except Exception:
            choices = []
            
        if not choices:
            choices = DEFAULT_SERVICE_CHOICES
            
        self.fields['service_type'] = forms.ChoiceField(
            choices=[('', 'Select service type')] + choices,
            widget=forms.Select(attrs={
                'class': 'form-field',
                'aria-label': 'Select service type',
                'required': True
            }),
            required=True,
            label='Service Type'
        )
