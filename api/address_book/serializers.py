from rest_framework import serializers
from .models import User, Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address', 'user']

    def create(self, validated_data):
        """
        Create and return a new `Address` instance, given the validated data.
        """
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Address` instance, given the validated data.
        """
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
