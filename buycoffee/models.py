import email
from django.db import models

# Create your models here.
class Order(models.Model):
   first_name=models.CharField(max_length=50)
   last_name=models.CharField(max_length=50)
   phone_number=models.CharField(max_length=30)
   email=models.EmailField
   order_size=models.IntegerField
   country=models.CharField(max_length=50)
   city=models.CharField(max_length=50)

   def __str__(self):
        return self.first_name
