
from django.db import models


class Flight(models.Model):
    FLIGHT_TYPES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=FLIGHT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price}"
