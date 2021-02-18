from django.db import models
from datetime import datetime

# Create your models here.
class Realtors(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now , blank=True)

    def __str__(self):
        return self.name
    
