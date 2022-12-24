from django.db.models import TextChoices


class OrderType(TextChoices):
    """Order type"""
    EXPRESS = "EXPRESS", "Express"
    PRIORITY = "PRIORITY", "Priority"
    STANDARD = "STANDARD", "Standard"
    OTHER = "OTHER", "Other"


class OrderMode(TextChoices):
    """The mode of shipment"""
    AIR = "AIR", "Air"
    LAND = "LAND", "Land"
    SEA = "SEA", "Sea"
    TRAIN = "TRAIN", "Train"


class OrderStatus(TextChoices):
    """The status of a shipment"""
    CREATED = "CREATED", "Created"
    IN_TRANSIT = "IN_TRANSIT", "In Transit"
    DELIVERED = "DELIVERED", "Delivered"
    LOST = "LOST", "Lost"
    RETURNED = "RETURNED", "Returned"
    HOLD = "ON_HOLD", "On Hold"
