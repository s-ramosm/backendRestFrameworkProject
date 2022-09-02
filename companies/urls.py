from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import companyView

router = DefaultRouter()

router.register(r'companies', companyView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
]