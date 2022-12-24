from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Order


class TrackingSerializer(serializers.Serializer):
    tracking_id = serializers.RegexField(r"[A-z]{2}[0-9]{8}[A-Z]{2}", required=True)


class OrderUpdateSerializer(serializers.Serializer):
    context = serializers.CharField()
    timeUpdated = serializers.DateTimeField(source="time_updated")


class OrderSerializer(serializers.Serializer):
    trackingId = serializers.CharField(source="tracking_id")
    shippedFrom = CountryField(source="shipped_from", country_dict=True)
    shippedTo = CountryField(source="shipped_to", country_dict=True)
    status = serializers.CharField()
    type = serializers.CharField()
    mode = serializers.CharField()
    expDelivery = serializers.DateField(source="exp_delivery")
    orderUpdates = OrderUpdateSerializer(many=True, source="updates")
