from django import forms
from bikeshop.models import Product

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 20)]

class CartAddProductForm(forms.Form):
    # def __init__(self, product, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(*args, **kwargs)
    #     self.fields['quantity'].choices = [(i, str(i)) for i in range(1, product.quantity + 1)]
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(attrs={'class':"form-control"}))
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)