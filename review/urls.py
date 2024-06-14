from django.urls import path

from .views import CommentViewSet, toggle_like

urlpatterns = [
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list-create'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
    path('toggle-like/<int:id>/', toggle_like, name='toggle-like'),
]
