from django import forms

from .models import Product 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'product_availability', 'price']



class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')
