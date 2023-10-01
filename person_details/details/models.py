from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Detailsm(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    dob=models.DateField(default=timezone.now)
    country_code=models.CharField(max_length=4,default='+91')
    contact=models.CharField(max_length=10)
    mail=models.EmailField()
    address=models.TextField()
    postal=models.CharField(max_length=10)
    city=models.CharField(max_length=15)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=15)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
