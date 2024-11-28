from django import forms
from .models import Mobile, Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nationality'}),
        }
        labels = {
            'name': 'Brand Name',
            'nationality': 'Nationality',
        }

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
