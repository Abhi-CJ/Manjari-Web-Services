from django.db import models

class Service(models.Model):
    """
    Model representing cab services offered (e.g., Local Cab, Airport Taxi).
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(
        blank=True,
        help_text='Raw SVG code for the service icon'
    )
    css_class = models.CharField(
        max_length=50,
        blank=True,
        help_text='CSS class for the service card, e.g. "airport-card"'
    )
    bullet_points = models.JSONField(
        default=list,
        help_text='List of bullet points to display on the service card'
    )

    class Meta:
        app_label = 'core'
        db_table = 'core_service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return str(self.title)
