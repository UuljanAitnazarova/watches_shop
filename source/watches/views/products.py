from django.contrib.auth.mixins import PermissionRequiredMixin
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
        queryset = Product.objects.filter(product_availability__gt=0).order_by('category', 'name')

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


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm
    permission_required = 'watches.add_product'

    def get_success_url(self):
        return reverse('product_list')


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    permission_required = 'watches.change_product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    permission_required = 'watches.delete_product'

    def get_success_url(self):
        return reverse('product_list')














