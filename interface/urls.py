from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("dog_identifier/", DogClassificationView.as_view(), name="interface_dog_identifier"),
    path("logout/", LogoutView.as_view(), name="interface_logout"),
    path("login/", LoginView.as_view(), name="interface_login"),
    path("privacy/", TemplateView.as_view(template_name="privacy.html"), name="interface_privacy"),
    path("terms_of_service/", TemplateView.as_view(template_name="terms_of_service.html"), name="interface_terms"),
    path("", HomeView.as_view(), name="interface_home"),
]
