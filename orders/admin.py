from django.contrib import admin

from orders.models import Order, WaitingListItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "robot_serial"]


@admin.register(WaitingListItem)
class WaitingListItemAdmin(admin.ModelAdmin):
    list_display = ["customer", "robot_serial"]
