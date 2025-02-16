from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


# Not using base User model to ensure email only auth
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please Ensure a Vaild Email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if extra_fields.get("is_staff") is False:
            raise ValueError("Superuser must also be staff")

        if extra_fields.get("is_superuser") is False:
            raise ValueError("Superuser must have is_superuser attribute = True")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField("Email", unique=True)
    password = models.CharField(max_length=250)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()


class Pizza(models.Model):
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
    crust = models.ForeignKey("Crust", on_delete=models.CASCADE)
    sauce = models.ForeignKey("Sauce", on_delete=models.CASCADE)
    cheese = models.ForeignKey("Cheese", on_delete=models.CASCADE)
    toppings = models.ManyToManyField("Toppings")


# Using Base field for easier adaptability, ie adding cost to each component
class PizzaField(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Size(PizzaField):
    pass


class Crust(PizzaField):
    pass


class Sauce(PizzaField):
    pass


class Cheese(PizzaField):
    pass


class Toppings(PizzaField):
    pass


class PaymentInfo(models.Model):
    name_on_card = models.CharField(max_length=50)
    card_num = models.IntegerField(
        validators=[MaxValueValidator(9999999999999999)]
    )  # 16 9s
    expiration_month = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    expiration_year = models.IntegerField(
        validators=[MinValueValidator(2025), MaxValueValidator(9999)]
    )
    cvv = models.IntegerField(
        MaxValueValidator(9999)
    )  # TODO Change to not save (Probably shouldn't be implemented like this)


class AddressInfo(models.Model):
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    eircode = models.CharField(max_length=10)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    payment = models.ForeignKey(PaymentInfo, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE)
    data_ordered = models.DateTimeField(auto_now_add=True)
