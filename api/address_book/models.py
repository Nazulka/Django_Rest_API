from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.address
