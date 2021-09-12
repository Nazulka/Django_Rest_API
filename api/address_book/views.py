from rest_framework import generics
from rest_framework import permissions
from .models import User, Address
from .serializers import UserSerializer, AddressSerializer
from address_book.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Address List': '/address-list/',
        'Address Detail View': 'address/<int:pk>/',
        'User List': 'users/',
        'User Details': 'users/<int:pk>/',
        # 'users': reverse('users-list', request=request, format=format),
        # 'address': reverse('address-list', request=request, format=format)
    })


class AddressList(generics.ListCreateAPIView):
    user = User.objects.all()
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
 

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/address-list/',
#         'Detail View': 'address-detail/<str:pk>/',
#         'Create': 'address-create/',
#         'Update': 'address-update/<str:pk>/',
#         'Delete': '/address-delete/<str:pk>',
#         }

#     return Response(api_urls)


# @api_view(['GET'])
# def addressList(request):
#     user = User.objects.all()
#     addresses = Address.objects.all()

#     user_serializer = UserSerializer(user, many=False)
#     address_serializer = AddressSerializer(addresses, many=True)
#     return Response({
#         'user': user_serializer.data,
#         'addresses': address_serializer.data
#     })


# @api_view(['GET'])
# def addressDetail(request, pk):
#     address = Address.objects.get(id=pk)
#     serializer = AddressSerializer(address, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def addressCreate(request):
#     serializer = AddressSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PUT'])
# def addressUpdate(request, pk):
#     user = Address.objects.get(id=pk)
#     serializer = AddressSerializer(instance=address, data=request.data)
#     data = {}
#     if serializer.is_valid():
#         serializer.save()
#         data['success'] = 'Update successful!'

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def addressDelete(request, pk):
#     address = Address.objects.get(id=pk)
#     address.delete()
#     return Response('User successfully deleted!')
