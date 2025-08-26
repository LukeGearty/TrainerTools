from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", RegisterView.as_view(), name="register"),
    path("add-client/", views.add_client, name="add_client"),
]
