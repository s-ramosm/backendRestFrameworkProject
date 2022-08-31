from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import userView

router = DefaultRouter()

router.register(r'users', userView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
]