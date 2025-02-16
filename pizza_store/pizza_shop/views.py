from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def index(request):
    if request.user.is_authenticated and isinstance(request.user, User):
        orders = Order.objects.filter(user=request.user)
    else:
        orders = None
    return render(request, "index.html")


@login_required
def order(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            request.session["pizza_id"] = pizza.id
            return redirect("enter_address")
    else:
        form = PizzaForm()

    return render(request, "order.html", {"form": form})


@login_required
def enter_address(request):
    if request.method == "POST":
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save()

            request.session["address_id"] = address.id

            return redirect("payment")
    else:
        address_form = AddressForm()

    return render(request, "enter_address.html", {"address_form": address_form})


@login_required
def payment(request):
    pizza_id = request.session.get("pizza_id")
    address_id = request.session.get("address_id")

    if not pizza_id or not address_id:
        return redirect("create_pizza")

    pizza = Pizza.objects.get(id=pizza_id)
    address = AddressInfo.objects.get(id=address_id)

    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()

            new_order = Order(
                user=request.user,
                pizza=pizza,
                address=address,
                payment=payment,
                data_ordered=timezone.now(),
            )
            new_order.save()

            request.session.pop("pizza_id", None)
            request.session.pop("address_id", None)

            return redirect("order_confimed")

    else:
        payment_form = PaymentForm()

    return render(
        request,
        "payment.html",
        {
            "pizza": pizza,
            "address": address,
            "payment_form": payment_form,
        },
    )


def confirmed_order(request):
    return render(request, "confirmed_order.html")


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class UserLoginView(LoginView):
    template_name = "login.html"


def logout_user(request):
    logout(request)
    return redirect("index")
