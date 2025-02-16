from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def index(request):
    if request.user.is_authenticated:
        orders = PizzaOrder.objects.filter(user=request.user)
    else:
        orders = None
    return render(request, "index.html")


def payment(request):
    return render(request, "index.html")


def confirmed_order(request):
    return render(request, "index.html")


@login_required
def order(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_order = form.save()
            newPizzaOrder = PizzaOrder(user=request.user, pizza=new_order, payment=None)
            newPizzaOrder.save()
            return redirect(payment)
        else:
            return (request, "order.html", {"form": form})
    else:
        form = PizzaForm()
        return render(request, "order.html", {"form": form})


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)


class UserLoginView(LoginView):
    template_name = "login.html"


def logout_user(request):
    logout(request)
    return redirect("/")
