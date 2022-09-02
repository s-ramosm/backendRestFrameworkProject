from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import stateView

router = DefaultRouter()

router.register(r'states', stateView, basename="state")

urlpatterns = [
    path('',include(router.urls)),
]