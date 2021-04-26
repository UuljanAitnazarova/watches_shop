from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from watches.models import Product, Order, ProductOrder
from watches.forms import OrderForm


class ProductAddCart(View):
    def get(self, request, pk):
        cart = request.session.get('cart', {})
        product = Product.objects.get(pk=pk)
        if product.product_availability > 0:
            try:

                cart[str(product.pk)] += 1
                product.product_availability -=1
                product.save()
            except KeyError:
                cart[product.pk] = 1
                product.product_availability -=1
                product.save()
            request.session['cart'] = cart
            print(request.session['cart'])
        return redirect('product_list')


class ProductRemoveCart(View):

    def post(self, request, pk):
        cart = request.session.get('cart', {})
        product = Product.objects.get(pk=pk)
        val = cart.get(str(pk))
        product.product_availability += val
        cart.pop(str(pk))
        product.save()
        request.session['cart'] = cart
        return redirect('cart')




class CartListView(ListView):
    template_name = 'cart/cart_view.html'
    context_object_name = 'items'

    def get_queryset(self):
        cart = self.request.session.get('cart', {})
        queryset = []
        for key, count in cart.items():
            product = {'product': Product.objects.get(pk=key), 'count': count}
            product['sum'] = count * product.get('product').price
            queryset.append(product)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for item in self.get_queryset():
            total += item['sum']
        context['total'] = total
        context['form'] = OrderForm()

        return context

class RegisterOrderView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        if form.is_valid():
            self.order = form.save(commit=False)
            if request.user.is_authenticated:
                self.order.user = request.user
                self.order.username = request.user.username
            self.order.save()
            self.makeorder()
            return redirect('product_list')
        return redirect('cart')



    def makeorder(self):
        cart = self.request.session.get('cart', {})
        for key, count in cart.items():
            product = {'product': Product.objects.get(pk=key), 'count': count}
            ProductOrder.objects.create(product_id=product['product'], order_id=self.order, units=product['count'])
            self.request.session['cart'] = {}


class OrdersView(LoginRequiredMixin, ListView):
    model = ProductOrder
    template_name = 'cart/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(order_id__user=self.request.user)










