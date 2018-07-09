from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ('pk','username','password','level','is_active')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Register.objects.create(username=validated_data.get('username'),password=validated_data.get('password'),level=validated_data.get('level'),is_active=validated_data.get('is_active'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.level = validated_data.get('level', instance.level)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        return instance


