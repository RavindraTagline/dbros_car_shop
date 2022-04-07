import datetime

from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


class Owner(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car Seller"


class Car(models.Model):
    CAR_CONDITION = [
        ('Select', 'Select'),
        ('Poor', 'Poor'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Excellent', 'Excellence'), ]
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, verbose_name="Seller Name")
    mobile = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Seller Mobile")
    make = models.CharField(max_length=120, blank=True, null=True)
    car_model = models.CharField(
        max_length=120, blank=True, null=True, verbose_name="Model")
    year_dropdown = []
    for y in range(2000, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))
    year = models.IntegerField(
        _('year'), choices=year_dropdown, default=datetime.datetime.now().year)
    condition = models.CharField(
        max_length=20, choices=CAR_CONDITION, default='Select')
    price = MoneyField(
        default=1000, default_currency="USD", max_digits=10, verbose_name="Asking Price", help_text="$1000 - $100,000",
        validators=[MinMoneyValidator(1000), MaxMoneyValidator(100000), ])
    STATUS = [('Available', 'Available'), ('Sold', 'Sold')]
    available = models.CharField(
        max_length=50, choices=STATUS, default='Available')

    def __str__(self):
        return self.car_model


class Buyer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=15)
    Net_amount = MoneyField(default_currency='USD', max_digits=10, default=0)

    @property
    def commission(self):
        self.a = self.car.Price
        return self.a * 5/100
