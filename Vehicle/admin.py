from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Buyer, Car, Owner


class CarInline(admin.StackedInline):
    model = Car


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        CarInline,
    ]


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'mobile', 'car_model', 'make',
                    'condition', 'year', 'price', 'available')
    list_filter = ('make', 'year')
    ordering = ('-id',)


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'buyer_name', 'mobile',
                    'commission', 'Net_amount')
    ordering = ('-id',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.unregister(Group)
admin.site.register(Buyer, BuyerAdmin)
admin.site.site_header = 'DodgyBros Administration'
