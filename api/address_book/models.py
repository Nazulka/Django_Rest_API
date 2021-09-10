from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    address_name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='UK')
    
    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address
