from rest_framework.exceptions import NotFound

from .models import Order


def get_order(**kwargs):
    try:
        return Order.objects.get(**kwargs)
    except Order.DoesNotExist:
        raise NotFound("Order not found")
