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
        user = is_admin = False
        user.email = self.cleaned_data["email"]
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
