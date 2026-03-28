from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Home_Property(models.Model):#property
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    price_max = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=100, default='Real Estate')
    image_main = models.ImageField(upload_to="Name", null=True, blank=True)
    image_person = models.ImageField(upload_to="Name", null=True, blank=True)
    location = models.CharField(max_length=255)

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Home_Property, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    notes = models.TextField(blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # or Confirmed, Cancelled
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add amount field

