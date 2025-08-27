from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Client
from .models import TrainerProfile
from django.contrib.auth.models import User


def manager_login(request):
    if request.user.is_authenticated:
        return redirect('manager-dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Optionally: check if the user is a manager
            if hasattr(user, 'trainerprofile') and user.trainerprofile.manager is not None:
                # This user is a trainer, not a manager
                messages.error(request, "You are not authorized to log in as a manager.")
            else:
                login(request, user)
                return redirect('manager_dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'manager/login.html')


@login_required
def manager_dashboard(request):
    trainers = TrainerProfile.objects.filter(manager=request.user)
    return render(request, "manager/dashboard.html", {"trainers": trainers})

@login_required
def manager_logout(request):
    logout(request)
    return redirect('manager_login')


@login_required
def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(TrainerProfile, pk=trainer_id, manager=request.user)
    clients = Client.objects.filter(trainer=trainer.user)
    return render(request, "manager/trainer_detail.html", {"trainer": trainer, "clients": clients})
