from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import scheduleView

router = DefaultRouter()

router.register(r'schedule', scheduleView, basename="state")

urlpatterns = [
    path('',include(router.urls)),
]