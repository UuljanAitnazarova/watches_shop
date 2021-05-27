from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, CartView, OrderApiView, get_token_view


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderApiView.as_view()),
    path('cart/', CartView.as_view()),
    path('token/', get_token_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]