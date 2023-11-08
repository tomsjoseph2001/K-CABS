from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    photo = models.CharField(max_length=500,default="A")
    housename= models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)



class Driver(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    photo = models.CharField(max_length=500,default="A")
    housename= models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    photo= models.CharField(max_length=100)


class Vehicle(models.Model):

    vehicleregno= models.CharField(max_length=20)
    vehiclemodel= models.CharField(max_length=10)
    enginenumber= models.CharField(max_length=10)
    totalseats= models.IntegerField()
    ac_nonac= models.CharField(max_length=10)
    vehicletype= models.CharField(max_length=25)
    photo= models.CharField(max_length=500)

class Complaint(models.Model):
    complaint= models.CharField(max_length=500)
    USER= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()
    status= models.CharField(max_length=20,default="pending")
    reply= models.CharField(max_length=20,default="pending")


class bank(models.Model):

    accountno= models.CharField(max_length=100)
    ifsccode= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    amount= models.FloatField(max_length=100)

class booking(models.Model):

    USER= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()

    pick=models.CharField(max_length=50)
    drop= models.CharField(max_length=50)
    status= models.CharField(max_length=50,default="booked ")
    VEHICLE= models.ForeignKey(Vehicle, on_delete=models.CASCADE)



class Carassign(models.Model):

    VEHICLE= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    DRIVER= models.ForeignKey(Driver, on_delete=models.CASCADE)