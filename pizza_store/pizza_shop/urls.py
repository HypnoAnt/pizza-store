from django.urls import path
from . import views
from . import forms
from .forms import *

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order"),
    path("payment", views.payment, name="payment"),
    path("order_confirmed", views.order_confirmed, name="order_confirmed"),
    path("enter_address", views.enter_address, name="enter_address"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("order_history/", views.order_history, name="order_history"),
]
