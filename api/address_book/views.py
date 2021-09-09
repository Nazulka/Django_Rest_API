from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Address
from .serializers import UserSerializer, AddressSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/address-list/',
        'Detail View': 'address-detail/<str:pk>/',
        'Create': 'address-create/',
        'Update': 'address-update/<str:pk>/',
        'Delete': '/address-delete/<str:pk>',
        }

    return Response(api_urls)


@api_view(['GET'])
def addressList(request):
    user = User.objects.all()
    addresses = Address.objects.all()

    user_serializer = UserSerializer(user, many=False)
    address_serializer = AddressSerializer(addresses, many=True)
    return Response({
        'user': user_serializer.data,
        'addresses': address_serializer.data
    })


@api_view(['GET'])
def addressDetail(request, pk):
    address = Address.objects.get(id=pk)
    serializer = AddressSerializer(address, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addressCreate(request):
    serializer = AddressSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def addressUpdate(request, pk):
    user = Address.objects.get(id=pk)
    serializer = AddressSerializer(instance=address, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'Update successful!'

    return Response(serializer.data)


@api_view(['DELETE'])
def addressDelete(request, pk):
    address = Address.objects.get(id=pk)
    address.delete()
    return Response('User successfully deleted!')
