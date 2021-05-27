from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from watches.models import Product, Order, ProductOrder
from api.serializers import ProductSerializer, OrderSerializer, BucketSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderApiView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BucketViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = BucketSerializer




