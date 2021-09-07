from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('address_book', views.UserView)

# Automatic URL routing + login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
]
