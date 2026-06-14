from django import forms
from core.models import Review
from core.constants import DEFAULT_REVIEW_RATING, MAX_REVIEW_RATING, MIN_REVIEW_RATING

class ReviewForm(forms.ModelForm):
    """
    Form for submitting customer reviews with accessibility attributes.
    """
    class Meta:
        model = Review
        fields = [
            'customer_name',
            'location',
            'rating',
            'review'
        ]
        
        labels = {
            'customer_name': 'Your Name',
            'location': 'Location',
            'rating': 'Rating (1-5 stars)',
            'review': 'Your Review'
        }
        
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Enter your name',
                'aria-label': 'Enter your name',
                'required': True
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'e.g., Gwalior',
                'aria-label': 'Enter your location',
                'required': True
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-field',
                'type': 'number',
                'min': str(MIN_REVIEW_RATING),
                'max': str(MAX_REVIEW_RATING),
                'value': str(DEFAULT_REVIEW_RATING),
                'aria-label': 'Rate your experience from 1 to 5 stars',
                'required': True
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-field',
                'placeholder': 'Tell us about your experience with Manjari Taxi...',
                'aria-label': 'Write your review',
                'rows': 4,
                'required': True
            })
        }