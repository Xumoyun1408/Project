from django import forms
from .models import Air,City

class AirForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    aholi = forms.IntegerField(widget=forms.TextInput({"class": "form-control", "type": "number"}))
    class Meta:
        model = Air
        fields = ['name','aholi','category','image']

class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    aholi = forms.IntegerField(widget=forms.TextInput({"class": "form-control", "type": "number"}))
    class Meta:
        model = City
        fields = ['name','aholi','reys','image']