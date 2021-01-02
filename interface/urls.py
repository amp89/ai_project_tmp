from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path("dog_identifier/", DogClassificationView.as_view(), name="interface_dog_identifier"),
    path("logout/", LogoutView.as_view(), name="interface_logout"),
    path("login/", LoginView.as_view(), name="interface_login"),
    path("", HomeView.as_view(), name="interface_home"),
]
