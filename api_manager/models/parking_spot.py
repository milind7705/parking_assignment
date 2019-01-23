from django.db import models
from django.contrib.gis.db import models
from rest_framework import serializers


class ParkingSlot(models.Model):
    """
    @summary: ParkingSlot Model
    """
    id = models.AutoField(primary_key=True)
    latitude = models.PointField(max_length=40, null=True)
    longitude = models.PointField(max_length=40, null=True)
    is_slot_available = models.BooleanField(default=True)
    place_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=15)

    class Meta(object):
        verbose_name = "ParkingSlot"
        verbose_name_plural = "ParkingSlots"
        app_label = 'api_manager'
        db_table = 'parking_slots'

    def __unicode__(self):
        return self.name


class ParkingSlotSerializer(serializers.ModelSerializer):
    """
    @summary: ParkingSlot Serializer
    """
    class Meta(object):
        model = ParkingSlot
        fields = ("id", "latitude", "longitude", "is_slot_available",
                  "place_name", "city", "country")
        depth = 1
