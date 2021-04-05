from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode

from watches.models import Product
from watches.forms import ProductForm, SearchForm


class ProductListView(ListView):
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 4
    paginate_orphans = 1

    def get(self, request, **kwargs):
        print(request.GET)
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductListView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.filter(product_availability__gt=0)

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            print(self.form.cleaned_data['search_value'])
            return self.form.cleaned_data['search_value']
        return None


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        return context




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('product_list')












# def product_list_view(request):
#     if request.GET.get('search_field'):
#         products = Product.objects.filter(name__contains=request.GET.get('search_field'))
#     else:
#         products = Product.objects.order_by('category', 'name')
#     return render(request, 'list.html', context={'products': products, "choices": Product.CATEGORY_CHOICE})
#
#
# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     return render(request, 'detail.html', context={'product':product})


# def product_create_view(request):
#     if request.method == 'GET':
#         form = ProductForm()
#         return render(request, 'product/product_create.html', context={'form': form})
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product = Product.objects.create(
#                 name = form.cleaned_data.get('name'),
#                 description = form.cleaned_data.get('description'),
#                 category = form.cleaned_data.get('category'),
#                 product_availability = form.cleaned_data.get('product_availability'),
#                 price = form.cleaned_data.get('price')
#             )
#             return redirect('product_detail', pk=product.id)
#         return render(request, 'product/product_create.html', context={'form':form})


# def product_update_view(request, pk):
#     product = get_object_or_404(Product, id=pk)
#
#     if request.method == 'GET':
#         form = ProductForm(initial={
#             'name' : product.name,
#             'description' : product.description,
#             'category' : product.category,
#             'product_availability' : product.product_availability,
#             'price' : product.price
#         })
#         return render(request, 'product/product_update.html', context={'form':form, 'product': product})
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data.get('name')
#             product.description = form.cleaned_data.get('description')
#             product.category = form.cleaned_data.get('category')
#             product.product_availability = form.cleaned_data.get('product_availability')
#             product.price = form.cleaned_data.get('price')
#             product.save()
#             return redirect('product_detail', pk=product.id)
#         return render(request, 'product/product_update.html', context={'form':form, 'product':product})


# def product_delete_view(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     if request.method == 'GET':
#         return render(request, 'product/product_delete.html', context={'product':product})
#     elif request.method ==  'POST':
#         product.delete()
#         return redirect('product_list')


