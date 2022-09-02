from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import userView,userSingUPview

router = DefaultRouter()

router.register(r'users', userView, basename="users")

urlpatterns = [
    path('users/crud/',include(router.urls)),
    path('singup/',  userSingUPview.as_view())
]