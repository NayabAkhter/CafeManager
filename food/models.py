from django.db import models
from django.contrib.auth.models import User

class Cuisine(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.category
class food(models.Model):
    category = models.ForeignKey(Cuisine, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    secondary_description = models.TextField(blank=True)  #can take blank value if value not given
    price = models.FloatField()
    is_available = models.BooleanField(default=True)   #default value
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    order_details = models.CharField(max_length=500)
    total_price = models.FloatField()
    is_ready = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upfated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

          
    