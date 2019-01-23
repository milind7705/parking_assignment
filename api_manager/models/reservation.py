from django.db import models
from rest_framework import serializers
from . import User, ParkingSlot


class Reservation(models.Model):
    """
    @summary: Reservation Model
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    parking_spot = models.ForeignKey(ParkingSlot)
    cost = models.IntegerField(null=False, default=0)

    class Meta(object):
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        app_label = 'api_manager'
        db_table = 'reservations'

    def __unicode__(self):
        return self.name


class ReservationSerializer(serializers.ModelSerializer):
    """
    @summary: Reservation Serializer
    """
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)
    parking_slot_id = serializers.PrimaryKeyRelatedField(
        queryset=ParkingSlot.objects.all(), source='parking_slots',
        write_only=True)

    class Meta(object):
        model = Reservation
        fields = ("id", "user", "parking_spot", "user_id", "parking_slot_id")
        depth = 2
