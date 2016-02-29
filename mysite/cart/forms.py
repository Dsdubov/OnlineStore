from django import forms
from bikeshop.models import Product

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)