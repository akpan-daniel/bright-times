from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import selectors
from .serializers import TrackingSerializer, OrderSerializer

# Create your views here.
class OrderTrack(APIView):
    def get(self, request):
        serializer = TrackingSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        response_data = selectors.get_order(**serializer.validated_data)
        response = {
            "data": OrderSerializer(response_data).data,
            "message": "Order retrieved",
        }

        return Response(response, status=status.HTTP_200_OK)
