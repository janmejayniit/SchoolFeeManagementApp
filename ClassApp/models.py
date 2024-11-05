from django.db import models
from django.forms import DateField

# Create your models here.
class ClassMaster(models.Model):
    name=models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
