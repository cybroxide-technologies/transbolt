from django.db import models
import uuid
# Create your models here.
class UserData(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=100 )
    lastName = models.CharField(max_length=100 )
    userType = models.CharField(max_length=100 )
    imgurl = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13 ,unique= True)
    email = models.EmailField(max_length=50 )
    lat = models.DecimalField(decimal_places=7 , max_digits=10)
    lng = models.DecimalField(decimal_places=7 , max_digits=10)
    password = models.CharField(max_length=200)
    fcmToken = models.CharField(max_length=500)

    
class VehicleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100 )
    regNo = models.CharField(max_length=100 )
    modelNo = models.CharField(max_length=100 )
    brandName = models.CharField(max_length=100 )
    liveUrl = models.CharField(max_length=100 )
    lat = models.DecimalField(decimal_places=7 , max_digits=10)
    lng = models.DecimalField(decimal_places=7 , max_digits=10)