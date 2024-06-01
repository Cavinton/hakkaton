from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, initial=1)

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=255)
    postal_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)