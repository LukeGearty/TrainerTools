from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    clients = Client.objects.filter(trainer=request.user)
    return render(request, 'core/dashboard.html', {"clients": clients})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("login")