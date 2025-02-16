from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
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

    pizza = Pizza.objects.get(id=pizza_id)
    address = AddressInfo.objects.get(id=address_id)

    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()

            # Create an Order object
            new_order = Order(
                user=request.user,
                pizza=pizza,
                address=address,
                payment=payment,
                data_ordered=timezone.now(),
            )
            new_order.save()

            # Save the order id in the session for later use
            request.session["order_id"] = new_order.id

            # Clear pizza and address from the session after placing the order
            request.session.pop("pizza_id", None)
            request.session.pop("address_id", None)

            return redirect("order_confirmed")  # Redirect to order confirmation page

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


@login_required
def order_confirmed(request):
    # Get the order ID from the session
    order_id = request.session.get("order_id")

    if not order_id:
        # If no order ID in session, redirect to an error page or back to the payment page
        return redirect(
            "error_page"
        )  # Replace with your actual error page URL or a different redirect

    # Try to retrieve the order from the database
    order = Order.objects.get(id=order_id)

    # Prepare context for the order confirmation page
    context = {
        "pizza": order.pizza,
        "address": order.address,
        "payment": order.payment,
    }

    return render(request, "order_confirmed.html", context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, "order_history.html", {"orders": orders})


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
