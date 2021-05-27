import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from watches.models import Product, Order, ProductOrder
from api.serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderApiView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartView(APIView):

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if cart:
            data = json.dumps(cart)
            print(data)
            return HttpResponse(data)
        response = JsonResponse({'error': 'no data in cart!'})
        response.status_code = 400
        return response


    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if request.body:
            data = json.loads(request.body)
            product = get_object_or_404(Product, id=data['product_id'])
            if product.product_availability >= 1:
                if not cart.get(str(data['product_id'])):
                    cart[str(data['product_id'])] = 1
                else:
                    cart[str(data['product_id'])] += 1
            else:
                return JsonResponse({'error': 'No available products'})
            request.session['cart'] = cart
            return JsonResponse(cart)
        response = JsonResponse({'error': 'No data provided!'})
        response.status_code = 400
        return response

    def delete(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        if request.body:
            data = json.loads(request.body)
            if cart.get(str(data['product_id'])):
                balance = cart[str(data['product_id'])] - 1
                if balance <= 0:
                    del cart[str(data['product_id'])]
                else:
                    cart[str(data['product_id'])] = balance
                request.session['cart'] = cart
                return JsonResponse({'Deleted': 'Deleted'})
            return JsonResponse({'error': 'No such product'})
        return JsonResponse({'error': 'No data provided!'})






@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')




