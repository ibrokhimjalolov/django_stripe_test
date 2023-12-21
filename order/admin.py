from django.contrib import admin
from order import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description")
    search_fields = ("name", "description")
