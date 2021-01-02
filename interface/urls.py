from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path("dog_identifier/", DogClassificationView.as_view(), name="interface_dog_identifier"),
    path("", HomeView.as_view(), name="interface_home"),
]
