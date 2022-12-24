from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.models import ClusterableModel, Orderable

from apps.core.models import BaseModel

from .enums import OrderMode, OrderStatus, OrderType


class Order(ClusterableModel, BaseModel):
    """A model that stores order info"""

    tracking_id = models.CharField(_("Tracking ID"), max_length=255, unique=True)
    shipped_from = CountryField(verbose_name=_("Shipping From"))
    shipped_to = CountryField(verbose_name=_("Shipping To"))
    is_delivered = models.BooleanField(_("Is Delivered?"), default=False)
    status = models.CharField(_("Shipping Status"), max_length=255, choices=OrderStatus.choices, default=OrderStatus.IN_TRANSIT)
    type = models.CharField(_("Shipping Type"), max_length=255, choices=OrderType.choices, default=OrderType.STANDARD)
    mode = models.CharField(_("Shipping Mode"), max_length=255, choices=OrderMode.choices, default=OrderMode.LAND)
    exp_delivery = models.DateField(_("Expected Delivery"))

    panels = [
        FieldPanel("tracking_id"),
        FieldPanel("shipped_from"),
        FieldPanel("shipped_to"),
        FieldPanel("is_delivered"),
        FieldPanel("status"),
        FieldPanel("type"),
        FieldPanel("mode"),
        FieldPanel("exp_delivery"),
        InlinePanel("updates"),
    ]


class OrderUpdate(Orderable, BaseModel):
    """A model to keep track of order status"""
    order = ParentalKey(to=Order, on_delete=models.CASCADE, related_name="updates")
    context = models.CharField(_("Context"), max_length=255)
    time_updated = models.DateTimeField(_("Time Updated"))

    panels = [
        FieldPanel("context"),
        FieldPanel("time_updated"),
    ]
