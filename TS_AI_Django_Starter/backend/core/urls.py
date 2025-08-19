from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProductViewSet, TaskViewSet, OrderViewSet,
    health, analytics, search, test_slow, test_error, test_echo, test_random
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('health', health),
    path('analytics', analytics),
    path('search', search),
    path('test/slow', test_slow),
    path('test/error/<int:code>', test_error),
    path('test/echo', test_echo),
    path('test/random', test_random),
]
