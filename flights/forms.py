

from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']
        widgets = {
            'type': forms.Select(choices=Flight.FLIGHT_TYPES)
        }