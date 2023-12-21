from django.contrib import admin
from order import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")


class OrderItemInline(admin.StackedInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = ("price",)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "get_total_price")
    readonly_fields = ("created_at", "get_total_price")
    inlines = [OrderItemInline]
