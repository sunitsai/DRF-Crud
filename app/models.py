from django.db import models

# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 