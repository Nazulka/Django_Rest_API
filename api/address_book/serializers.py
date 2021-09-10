from rest_framework import serializers
from .models import User, Address


class UserSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Address.objects.all())

    class Meta:
        model = User
        fields = ['id', 'name', 'address']


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

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
