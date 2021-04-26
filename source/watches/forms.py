from django import forms

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'product_availability', 'price']



class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'address']
