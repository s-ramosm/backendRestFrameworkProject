from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import accessPointView

router = DefaultRouter()

router.register(r'accessPoints', accessPointView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
]