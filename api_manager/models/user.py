from django.db import models
from rest_framework import serializers


class User(models.Model):
    """
    @summary: Category Model
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    email_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta(object):
        verbose_name = "User"
        verbose_name_plural = "Users"
        app_label = 'api_manager'
        db_table = 'user'

    def __unicode__(self):
        return self.name


class UserSerializer(serializers.ModelSerializer):
    """
    @summary: User Serializer
    """

    class Meta(object):
        model = User
        fields = ("id", "name", "password", "phone_number", "email_id")
        depth = 1
