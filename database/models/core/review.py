from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    """
    Model representing customer testimonials.
    """
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'core'
        db_table = 'core_review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self) -> str:
        return str(self.customer_name)
