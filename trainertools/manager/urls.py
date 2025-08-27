from django.urls import path
from . import views

urlpatterns = [
    path("", views.manager_dashboard, name="manager_dashboard"),
    path("trainer/<int:trainer_id>/", views.trainer_detail, name="trainer_detail"),
    path("login/", views.manager_login, name="manager_login"),
    path("logout/", views.manager_logout, name="manager_logout"),


]
