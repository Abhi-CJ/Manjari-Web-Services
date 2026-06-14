from django.db import models

class Vehicle(models.Model):
    """
    Model representing active cabs in the fleet.
    """
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='vehicles/')
    seats = models.IntegerField(default=4)
    features = models.JSONField(
        default=list,
        help_text='List of features, e.g. ["AC", "Luggage Space", "Music System"]'
    )

    class Meta:
        app_label = 'core'
        db_table = 'core_vehicle'
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self) -> str:
        return str(self.name)
