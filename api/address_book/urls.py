from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('users', views.UserView)

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('address-list/', views.addressList, name='address-list'),
    path('address-detail/<str:pk>/', views.addressDetail, name='address-detail'),
    path('address-create/', views.addressCreate, name='address-create'),
    path('address-update/<str:pk>/', views.addressUpdate, name='address-update'),
    path('address-delete/<str:pk>/', views.addressDelete, name='address-delete'),
]
