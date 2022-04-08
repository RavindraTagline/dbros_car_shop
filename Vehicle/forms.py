from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class BuyerForm(forms.Form):
    name = forms.CharField(max_length=120)
    #hellow
    mobile = forms.CharField(max_length=15)
