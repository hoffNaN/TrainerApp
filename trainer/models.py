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
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    verbose_name='Nazwa użytkownika')
    name = models.CharField(max_length=20,
    verbose_name='Imię i Nazwisko')
    dayofbirth = models.DateTimeField(verbose_name='Wiek')
    interests = models.TextField(max_length=200,
    verbose_name='Zainteresowania')
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE,
    verbose_name='Kontakt')
    discription = models.TextField(max_length=400,
    verbose_name='O Sobie')
    sex_choices = (
    ('KOBIETA', 'K'),
    ('MĘŻCZYZNA', 'M'),
    )
    sex = models.CharField(max_length=1,
    choices=sex_choices,
    verbose_name='Płeć')
    address =  models.ForeignKey('Address', on_delete=models.CASCADE,
    verbose_name='Skąd')
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE,
    null=True,
    verbose_name='Jestem trenerem')
    gymowner = models.ForeignKey('GymOwner', on_delete=models.CASCADE,
    null=True,
    verbose_name='Jestem właścicielem obiektu')

class Trainer(models.Model):
    qualifications = models.TextField(max_length=60,
    verbose_name='Kwalifikacje')
    gym = models.ManyToManyField('Gym', blank=True, verbose_name='Siłownia')
    experience = models.TextField(max_length=60, verbose_name='Doświadczenie')
    specialization = models.ForeignKey('TrainType', on_delete=models.CASCADE,
    verbose_name='Specjalizacje')
    rating = models.ForeignKey('Opinion', on_delete=models.CASCADE, null=True,
     verbose_name='Opinia')
    offert = models.ForeignKey('Offer', on_delete=models.CASCADE, null=True,
    verbose_name='Oferta')

class GymOwner(models.Model):
    gym = models.ManyToManyField('Gym', blank=True, verbose_name='Siłownia')
    offert = models.ForeignKey('Offer', on_delete=models.CASCADE, null=True,
    verbose_name='Oferta')

class Address(models.Model):
    country_code = models.CharField(max_length=3, verbose_name='Kod kraju')
    province = models.CharField(max_length=20, verbose_name='Województwo')
    city = models.CharField(max_length=30, verbose_name='Miasto')


class Contact(models.Model):
    phone = models.CharField(max_length=9, verbose_name='Numer telefonu')
    email = models.EmailField(verbose_name='Adres email')
    fb = models.CharField(max_length=30, verbose_name='Facebook')

class Gym(models.Model):
    name_gym = models.CharField(max_length=20, verbose_name='Nazwa siłowni')
    discription = models.TextField(max_length=400, verbose_name='Opis')
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE,
    verbose_name='Kontakt')
    #trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True)
    offert = models.ForeignKey('TrainType', on_delete=models.CASCADE,
    verbose_name='Oferta')

class TrainType(models.Model):
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

    train_type = models.CharField(max_length=5, choices=train_choice,
    default=JOGA, verbose_name='Typ treningu')

class Offer(models.Model):
    discription = models.TextField(max_length=200,
    verbose_name='Opis')
    price = models.DecimalField(max_digits=8, decimal_places=2,
    verbose_name='Cena')
    train_type = models.ForeignKey('TrainType', on_delete=models.CASCADE,
    verbose_name='Typ treningu')
    localization = models.ForeignKey('Address', on_delete=models.CASCADE,
    verbose_name='Lokalizacja')

class Opinion(models.Model):
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

    opinion_type = models.CharField(max_length=5, choices=rating_choice,
    default=NEUTRAL, verbose_name='Opinia')
