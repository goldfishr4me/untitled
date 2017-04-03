from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .. import models


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = ('name', 'age')



