from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import countryView

router = DefaultRouter()

router.register(r'countries', countryView, basename="country")

urlpatterns = [
    path('',include(router.urls)),
]