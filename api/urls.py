from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = SimpleRouter()
router.register('groups', GroupViewSet, basename = 'groups')
router.register('posts', PostViewSet, basename = 'posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename = 'comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
