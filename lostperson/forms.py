from django import forms
from .models import LostPerson

class LostPersonForm(forms.ModelForm):
    class Meta:
        model = LostPerson
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


