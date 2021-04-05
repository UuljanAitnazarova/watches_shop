from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from watches.models import Product, ProductCart, Order, ProductOrder
from watches.forms import OrderForm


class ProductAddCart(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product.product_availability > 0:
            try:
                cart = ProductCart.objects.get(product=product)
                cart.units +=1
                product.product_availability -=1
                cart.save()
                product.save()
            except:
                ProductCart.objects.create(product=product, units=1)
                product.product_availability -=1
                product.save()
        return redirect('product_list')


class ProductRemoveCart(View):
    def post(self, request, pk):
        cart = get_object_or_404(ProductCart, pk=pk)
        product = Product.objects.get(pk=cart.product.pk)
        product.product_availability += cart.units
        cart.delete()
        product.save()
        return redirect('cart')




class CartListView(ListView):
    model = ProductCart
    template_name = 'cart/cart_view.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        items = ProductCart.objects.all()
        context['product_sum'] = []
        total = 0
        for item in items:
            product_sum = item.units * item.product.price
            context['product_sum'].append({'item': item, "total": product_sum})
            total += product_sum
        context['total'] = total
        context['form'] = OrderForm()

        return context

class RegisterOrderView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        if form.is_valid():
            self.order = form.save()
            self.makeorder()
            return redirect('product_list')
        return redirect('cart')



    def makeorder(self):
        for cart in ProductCart.objects.all():
            ProductOrder.objects.create(product_id=cart.product, order_id=self.order, units=cart.units)
        ProductCart.objects.all().delete()




