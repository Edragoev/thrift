from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# models.py
class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
