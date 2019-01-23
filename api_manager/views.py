from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import User, UserSerializer, Reservation, ReservationSerializer, \
    ParkingSlot, ParkingSlotSerializer
from rest_framework.views import APIView
from rest_framework import status, response
from rest_framework.decorators import api_view


class MyViewSet(NestedViewSetMixin, CreateModelMixin, RetrieveModelMixin,
                DestroyModelMixin, ListModelMixin, GenericViewSet,
                UpdateModelMixin):
    """
    @summary: viewset for all the operations
    """
    pass


class UserViewSet(MyViewSet):
    """
    @summary: viewset for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationViewSet(MyViewSet):
    """
    @summary: viewset for users
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ParkingSlotView(APIView):
    """
    @summary: api_view for parking slots
    """
    def get(self, request):
        """
        @summary: get call for available parking slots and search
        @param request: Request object
        """
        if not request.query_params:
            parking_slots = ParkingSlotSerializer(
                 ParkingSlot.objects.filter(
                     is_slot_available=True), many=True).data
        else:
            # logic to get the parking slots for that said radius
            params = request.query_params
            latitude = params.get("latitude")
            longitude = params.get("longitude")
            radius = params.get("radius")

        return response.Response(status=status.HTTP_200_OK, data=parking_slots)


@api_view(['GET'])
def get_reservation_cost(request):
    """
    @summary: GET API for fetching the reservation cost
    @param request: Request object
    """
    param = request.query_params
    user_id = param.get("user_id")
    if not user_id:
        msg = "The user_id filters are not provided"
        return response.Response(status=status.HTTP_400_BAD_REQUEST, data=msg)
    reservations = ReservationSerializer(
        Reservation.objects.filter(user__id=user_id), many=True).data
    parking_cost = sum([reservation.get('cost')
                        for reservation in reservations])
    return response.Response(status=status.HTTP_200_OK, data=parking_cost)
