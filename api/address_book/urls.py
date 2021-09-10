from django.urls import path, include
from address_book import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('address-list/', views.AddressList.as_view()),
    path('address/<int:pk>/', views.AddressDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('rest-auth/', include('rest_framework.urls')),
    # path('address-detail/<str:pk>/', views.addressDetail, name='address-detail'),
    # path('address-create/', views.addressCreate, name='address-create'),
    # path('address-update/<str:pk>/', views.addressUpdate, name='address-update'),
    # path('address-delete/<str:pk>/', views.addressDelete, name='address-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
