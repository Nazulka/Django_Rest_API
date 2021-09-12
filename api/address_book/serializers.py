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
    address_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(required=True, max_length=100)
    country = serializers.CharField(max_length=100, default='UK')

    class Meta:
        model = Address
        fields = ['id', 'user', 'address_name', 'address', 'country']

    def create(self, validated_data):
        """
        Create and return a new `Address` instance, given the validated data.
        """
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Address` instance, given the validated data.
        """
        instance.address_name = validated_data.get(
            'address_name', instance.address_name)
        instance.address = validated_data.get('address', instance.address)
        instance.country = validated_data.get('country', instance.country)

        instance.save()
        return instance
