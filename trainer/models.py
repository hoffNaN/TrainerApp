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
    qualifications = models.TextField(max_length=60)
    gym = models.ManyToManyField('Gym', blank=True)
    experience = models.TextField(max_length=60)
    specialization = models.ForeignKey('TrainType', on_delete=models.CASCADE)
    rating = models.ManyToManyField()
    offert = models.ForeignKey('Offer', on_delete=models.CASCADE, null=True)

class GymOwner(models.Model):
    gym = models.ManyToManyField('Gym', blank=True)
    offert = models.ForeignKey('Offer', on_delete=models.CASCADE, null=True)


class Address(models.Model):
    country_code = models.CharField(max_length=3)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

class Contact(models.Model):
    phone = models.CharField(max_length=9)
    email = models.EmailField()
    fb = models.CharField(max_length=30)

class Gym(models.Model):
    name_gym = models.CharField(max_length=20)
    discription = models.TextField(max_length=400)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True)
    offert = models.ForeignKey('TrainType', on_delete=models.CASCADE)

class TrainType(models.model):
    JOGA = 'joga'
    TBC = 'tbc'
    FITNESS = 'fitness'
    CROSSFIT = 'crossfit'
    train_choice = (
        (JOGA, 'joga'),
        (TBC, 'tbc'),
        (FITNESS, 'fitness'),
        (CROSSFIT, 'crossfit'),
    )

    train_type = models.CharField(max_length=5, choices=train_choice, default=JOGA)

class Offer(models.model):
    discription = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    train_type = models.ForeignKey('TrainType', on_delete=models.CASCADE)
    localization = models.ForeignKey('Address', on_delete=models.CASCADE)

class Opinion(models.model):
    WORSE = 'worse'
    BAD = 'bad'
    NEUTRAL = 'neutral'
    GOOD = 'good'
    BEST = 'best'
    rating_choice = (
        (WORSE, 'worse'),
        (BAD, 'bad'),
        (NEUTRAL, 'neutral'),
        (GOOD, 'good'),
        (BEST, 'best')
    )

    opinion_type = models.CharField(max_length=5, choices=rating_choice, default=NEUTRAL)
