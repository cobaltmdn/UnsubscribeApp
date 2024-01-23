from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    address = models.EmailField()

    def __str__(self):
        return self.address