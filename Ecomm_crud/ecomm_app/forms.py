from django import forms
from .models import ecomm_model

class ecomm_form(forms.ModelForm):
    class Meta:
        model = ecomm_model
        fields = ['name','phone','email','product','quantity']
