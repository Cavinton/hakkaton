from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductListView

router = DefaultRouter()
router.register('product', ProductListView)

urlpatterns = [
    path('', include(router.urls))
]