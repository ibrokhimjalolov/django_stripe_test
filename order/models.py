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
