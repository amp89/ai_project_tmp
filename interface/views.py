from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")