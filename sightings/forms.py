from django import forms
from .models import Sighting

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['lost_person', 'sighting_location', 'description', 'contact_information', 'image']
