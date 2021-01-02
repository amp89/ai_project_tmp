from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class DogClassificationView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "dog_classification.html")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "logout_confirmation.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")