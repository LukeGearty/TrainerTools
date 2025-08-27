from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import ClientForm


@login_required
def dashboard(request):
    clients = Client.objects.filter(trainer=request.user)
    return render(request, 'core/dashboard.html', {"clients": clients})

@login_required
def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.trainer = request.user
            client.save()
            return redirect("dashboard")
    else:
        form = ClientForm()
    return render(request, "core/add_client.html", {"form": form})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk, trainer=request.user)
    return render(request, "core/client_detail.html", {"client": client})

@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk, trainer=request.user)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_detail", pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, "core/edit_client.html", {"form": form, "client":client})

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk, trainer=request.user)
    if request.method == "POST":
        client.delete()
        return redirect("dashboard")
    return render(request, "core/delete_client.html", {"client": client})

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("login")