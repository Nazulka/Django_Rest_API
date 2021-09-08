from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('users', views.UserView)

# Automatic URL routing + login URLs for the browsable API
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-update/<str:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<str:pk>/', views.userDelete, name='user-delete'),
]
