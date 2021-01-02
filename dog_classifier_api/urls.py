from django.urls import path
from django.urls import include

from .views import *


urlpatterns = [
    path("health_check/", HealthCheckView.as_view(), name="dog_classifier_api_health_check"),
    path("auth_health_check/", AuthHealthCheckView.as_view(), name="dog_classifier_api_auth_health_check"),
    path("classify/", DogClassifierView.as_view(), name="dog_classifier_api_classify"),

]
