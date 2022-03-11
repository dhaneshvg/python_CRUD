from django import forms

from .models import product


class ModelForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'desc', 'price', 'img']
