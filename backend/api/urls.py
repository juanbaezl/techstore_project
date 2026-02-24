from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.category import CategoryViewSet
from api.views.hello_world import HelloWorldView
from api.views.product import ProductViewSet

# create a router
router = DefaultRouter()

# register routes to the api Router
router.register(r"hello", HelloWorldView, basename="hello")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")

# Wire up our API using automatic URL routing
urlpatterns = [
    path("", include(router.urls)),
]
