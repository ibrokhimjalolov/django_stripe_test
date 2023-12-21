from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))
    price = models.PositiveIntegerField(_("Price"), help_text="cent")  # price will store in minimum unit
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        ordering = ["name"]
        db_table = "items"


class OrderStatus(models.TextChoices):
    CREATED = "created", _("Created")
    PAID = "paid", _("Paid")
    CANCELED = "canceled", _("Canceled")
    REFUNDED = "refunded", _("Refunded")
    

class Order(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    status = models.CharField(_("Status"), max_length=255, default="created", choices=OrderStatus.choices)
    paid_at = models.DateTimeField(_("Paid at"), null=True, blank=True)
    
    def get_total_price(self) -> int:
        return sum([item.price * item.quantity for item in self.items.all()])
    
    def __str__(self) -> str:
        return f"Order #{self.id}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ["-id"]
        db_table = "orders"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, verbose_name=_("Item"), on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(_("Quantity"))
    price = models.PositiveIntegerField(_("Price"), help_text="cent", editable=False)
    
    def __str__(self) -> str:
        return str(self.item)
    
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ["-id"]
        db_table = "order_items"
        unique_together = ["order", "item"]

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.item.price
        super().save(*args, **kwargs)
