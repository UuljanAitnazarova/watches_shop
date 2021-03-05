from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', context={'products': products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', context={'product':product})


def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name = form.cleaned_data.get('name'), 
                description = form.cleaned_data.get('description'),
                category = form.cleaned_data.get('category'),
                product_availability = form.cleaned_data.get('product_availability'),
                price = form.cleaned_data.get('price')
            )
            return redirect('product_detail', pk=product.id)
        return render(request, 'product_create', context={'form':form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        form = ProductForm(initial={
            'name' : product.name,
            'description' : product.description,
            'category' : product.category,
            'product_availability' : product.product_availability,
            'price' : product.price
        })
        return render(request, 'product_update.html', context={'form':form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.product_availability = form.cleaned_data.get('product_availability')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('product_detail', pk=product.id)
        return render(request, 'product_update.html', context={'form':form, 'product':product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product':product})
    elif request.method ==  'POST':
        product.delete()
        return redirect('product_list')