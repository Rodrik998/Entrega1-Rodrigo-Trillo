from django import forms

class ProductForms(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)

class CategoryForms(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)

class ProviderForms(forms.Form):
    name = forms.CharField(max_length=50)
    provides = forms.CharField(max_length=100)