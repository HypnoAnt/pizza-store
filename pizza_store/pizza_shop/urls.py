from django.urls import path
from . import views
from . import forms
from .forms import *

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order"),
    path("payment", views.payment, name="payment"),
    path("confirmed_order", views.confirmed_order, name="confirmed_order"),
    path("register", views.UserRegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.logout, name="logout"),
]
