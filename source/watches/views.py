from django.shortcuts import render, get_object_or_404

from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', context={'products': products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', context={'product':product})