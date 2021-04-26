from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductAddCart,
    CartListView,
    ProductRemoveCart,
    RegisterOrderView,
    OrdersView,
    )

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/cart/', ProductAddCart.as_view(), name='add_cart'),
    path('order/', RegisterOrderView.as_view(), name='order'),
    path('cart/<int:pk>', ProductRemoveCart.as_view(), name='remove_cart'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('orders/', OrdersView.as_view(), name='orders'),
]