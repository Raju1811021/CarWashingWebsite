from django.db import models

# Create your models here.
class carprice(models.Model):
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    def __str__(self):
        return self.carname
class Booking_Details(models.Model):
    name=models.CharField(max_length=30)
    car_no=models.CharField(max_length=4)
    address=models.TextField(max_length=500)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.name