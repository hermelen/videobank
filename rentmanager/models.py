# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

# Create your models here.


class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')


# GENRE = [
#     ("action", "Action"),
#     ("romance", "Romance"),
#     ("science-fiction", "Science-Fiction"),
#     ("comedie-musicale", "Comédie Musicale"),
#     ("historique", "Historique"),
#     ("arts-martiaux", "Arts-Martiaux"),
# ]


class MovieGenre(models.Model):
    label = models.CharField(max_length = 100, verbose_name="Genre", null=True, blank=True)
    slug  = AutoSlugField(populate_from='label', verbose_name="Slug", null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.label


class Actor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Prénom", null=True, blank=True)
    last_name  = models.CharField(max_length=100, verbose_name="Nom", null=True, blank=True)
    picture    = models.ImageField(null=True, blank=True, upload_to="actors", verbose_name="Photo")
    # movies     = models.ManyToManyField('Movie', blank=True)

    def __unicode__(self):
        return self.last_name


class Director(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Prénom", null=True, blank=True)
    last_name  = models.CharField(max_length=100, verbose_name="Nom", null=True, blank=True)
    picture    = models.ImageField(null=True, blank=True, upload_to="directors", verbose_name="Photo")

    def __unicode__(self):
        return self.last_name



class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pays", null=True, blank=True)

    def __unicode__(self):
        return self.name



class Movie(models.Model):
    genre        = models.ForeignKey(MovieGenre,on_delete=models.CASCADE)
    # actors       = models.ForeignKey(Actor,on_delete=models.CASCADE, null=True, blank=True)
    actors       = models.ManyToManyField('Actor', blank=True, related_name='movies')
    country      = models.ForeignKey(Country,on_delete=models.CASCADE, null=True, blank=True)
    director     = models.ForeignKey(Director,on_delete=models.CASCADE, null=True, blank=True)
    lenght       = models.TimeField(max_length=100, verbose_name="Durée", null=True, blank=True)
    picture      = models.ImageField(null=True, upload_to="covers", verbose_name="Photo")
    release_date = models.DateTimeField()
    rented       = models.BooleanField()
    slug         = AutoSlugField(populate_from='title', verbose_name="Slug", null=True, blank=True, unique=True)
    synopsis     = models.TextField(null=True, blank=True)
    title        = models.CharField(max_length=100, verbose_name="Titre", null=True, blank=True)
    trailer_url  = models.URLField( null=True, blank=True)

    def __unicode__(self):
        return self.title



class MovieRent(models.Model):
    customer      = models.ForeignKey(Customer,on_delete=models.CASCADE)
    movies        = models.ForeignKey(Movie,on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now=True)
    return_date   = models.DateTimeField()

    # def __unicode__(self):
    #     return self.name
