from django.urls import path, include
from .models import *
from rest_framework import routers
from .api_views import *

router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('filter/', ProductListView.as_view(),name= 'filter'),
    path('product/<int:pk>/', ProductDetail.as_view(),name='product'),

]