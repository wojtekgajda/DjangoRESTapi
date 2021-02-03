from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AdditionalInfo(models.Model):
    TYPES = [
        (0, 'Unknown'),
        (1, 'Sci-fi'),
        (2, 'Horror'),
        (3, 'Drama'),
        (4, 'Comedy'),
        (5, 'Document'),

    ]

    duration = models.IntegerField()
    type = models.IntegerField(choices=TYPES, default=0)


class Film(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    after_premier = models.BooleanField(default=False)
    premier = models.DateField(null=True, blank=True)
    release_year = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name()

    def name(self):
        return self.title + '(' + str(self.release_year) + ')'


class Review(models.Model):
    review = models.TextField(max_length=1023, default='')
    star_rate = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.review


class Actor(models.Model):
    f_name = models.CharField(max_length=32)
    l_name = models.CharField(max_length=32)
    movies = models.ManyToManyField(Film)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
