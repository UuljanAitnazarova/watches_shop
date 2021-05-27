from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, BucketViewSet, OrderApiView


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'bucket', BucketViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]