from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [


    path("", HomeView.as_view(), name="interface_home"),
]
