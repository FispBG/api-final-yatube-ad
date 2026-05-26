from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),

    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='comments'
    ),

    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='comment-detail'
    ),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
