from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Client



@login_required
def dashboard(request):
    clients = Client.objects.filter(trainer=request.user)
    return render(request, 'core/dashboard.html', {"clients": clients})

