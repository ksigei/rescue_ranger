from django import forms
from .models import LostPerson

class LostPersonForm(forms.ModelForm):
    class Meta:
        model = LostPerson
        fields = '__all__'  
