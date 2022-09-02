from rest_framework.routers import DefaultRouter
from django.urls import path, include
<<<<<<< HEAD
from .views import userView,userSingUPview
=======
from .views import userView
>>>>>>> bc0aa42eb524c864ff3798b3593e67eeba68c8d0

router = DefaultRouter()

router.register(r'users', userView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
<<<<<<< HEAD
    # path('singup/',  userSingUPview.as_view())
=======
>>>>>>> bc0aa42eb524c864ff3798b3593e67eeba68c8d0
]