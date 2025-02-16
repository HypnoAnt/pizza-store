from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import (
    ModelForm,
    ModelChoiceField,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple,
)
from .models import *
from .forms import *
from django.db import transaction


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "password1", "password2"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data["email"]
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust", "sauce", "cheese", "toppings"]

    toppings = forms.ModelMultipleChoiceField(
        queryset=Toppings.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = [
            "name_on_card",
            "card_num",
            "expiration_month",
            "expiration_year",
            "cvv",
        ]
        labels = {
            "name_on_card": "Full Name",
            "card_num": "Card Number",
            "expiration_month": "Expiry Month",
            "expiration_year": "Expiry Year",
            "cvv": "CVV",
        }
        widgets = {
            "card_num": forms.NumberInput(
                attrs={"pattern": "[0-9]{15,16}", "title": "15 digits required"}
            ),
            "expiration_month": forms.TextInput(
                attrs={"pattern": "[0-9]{2}", "title": "2 digits required"}
            ),
            "expiration_year": forms.TextInput(
                attrs={"pattern": "[0-9]{4}", "title": "4 digits required"}
            ),
            "cvv": forms.TextInput(
                attrs={"pattern": "[0-9]{3,4}", "title": "3 digits required"}
            ),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressInfo
        fields = ["address_line_1", "address_line_2", "country", "eircode"]
        labels = {
            "address_line_1": "Address Line",
            "address_line_2": "Address Line 2",
            "country": "Country",
            "eircode": "Eircode",
        }
        widgets = {
            "address_line_1": forms.TextInput(attrs={"class": "form-control"}),
            "address_line_2": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "eircode": forms.TextInput(attrs={"class": "form-control"}),
        }
