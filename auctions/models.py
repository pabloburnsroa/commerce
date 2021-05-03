from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    """ Model for auction listing """
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f"{self.title}: is ${self.price} and is being sold by {self.owner}"

class Bid(models.Model):
    """ Model for representing a bid in an auction """ 
    time = models.DateTimeField(auto_now_add=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    
    def __str__(self):
       return f"{self.user} placed a bid for ${self.price}"