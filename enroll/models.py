from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MyDataModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name
