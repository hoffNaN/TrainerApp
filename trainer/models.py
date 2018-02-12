from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class BasicUser(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dayofbirth = models.DateTimeField
    interests = models.TextField(max_length=200)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    discription = models.TextField(max_length=400)
    sex = models.CharField(max_length=1)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True)
    gymowner = models.ForeignKey('GymOwner', on_delete=models.CASCADE, null=True)

class Trainer(models.Model):
    qualify = models.TextField(max_length=60)
    gym = models.CharField(max_length=10)
    experience = models.TextField(max_length=60)
    spec = models.CharField(max_length=200)
    opinion = models.Charfield(max_length=1)

class GymOwner(models.Model):
    gym = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)

class Address(models.Model):
    country_code = models.CharField(max_length=3)
    province = model.CharField(max_length=20)
    city = model.CharField(max_length=30)

class Contact(models.Model):
    phone = models.CharField(max_length=9)
    email = models.CharField(max_length=25)
    fb = models.CharField(max_length=30)

class Gym(models.Model):
    
