from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20)
    country = models.CharField(default='UK', max_length=100)

    def __str__(self):
        return self.last_name
