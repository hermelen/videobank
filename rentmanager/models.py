# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

from django.urls import reverse

from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')

    class Meta:
        verbose_name = _('customer')



class MovieGenre(TranslatableModel):
    translations = TranslatedFields(
        label = models.CharField(max_length = 100, verbose_name=_('genre'), null=True, blank=True),
        slug  = AutoSlugField(populate_from='label', verbose_name=_('slug'), null=True, blank=True, unique=True),
    )

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _('genre')


class Actor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name  = models.CharField(max_length=100, verbose_name=_('last name'))
    picture    = models.ImageField(null=True, blank=True, upload_to="actors", verbose_name=_('picture'))


    def __unicode__(self):
        display_name = self.last_name.upper() + ' ' + self.first_name.capitalize()
        return display_name

    class Meta:
        verbose_name = _('actor')


class Director(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'), null=True, blank=True)
    last_name  = models.CharField(max_length=100, verbose_name=_('last name'), null=True, blank=True)
    picture    = models.ImageField(null=True, blank=True, upload_to="directors", verbose_name=_('picture'))

    def __unicode__(self):
        display_name = self.last_name.upper() + ' ' + self.first_name.capitalize()
        return display_name

    class Meta:
        verbose_name = _('director')



class Country(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name=_('name'), null=True, blank=True),
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')



class Movie(TranslatableModel):
    translations = TranslatedFields(
      title        = models.CharField(max_length=100, verbose_name=_('title')),
      synopsis     = models.TextField(null=True, blank=True, verbose_name=_('synopsis')),
      slug         = AutoSlugField(populate_from='title', null=True, blank=True, unique=True, always_update=True, verbose_name=_('slug')),
    )
    genre        = models.ForeignKey(MovieGenre,on_delete=models.CASCADE, verbose_name=_('genre'))
    actors       = models.ManyToManyField('Actor', blank=True, related_name='movies', verbose_name=_('actors'))
    country      = models.ForeignKey(Country,on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('country'))
    director     = models.ForeignKey(Director,on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('director'))
    lenght       = models.TimeField(max_length=100, null=True, blank=True, verbose_name=_('lenght'))
    picture      = models.ImageField(null=True, upload_to="covers", verbose_name=_('picture'))
    release_date = models.DateTimeField(verbose_name=_('release date'))
    rented       = models.BooleanField(default=False, verbose_name=_('rented'))
    trailer_url  = models.URLField( null=True, blank=True, verbose_name=_('trailer url'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[self.slug])

    class Meta:
        verbose_name = _('movie')



class MovieRent(models.Model):
    customer      = models.ForeignKey(Customer,on_delete=models.CASCADE)
    movies        = models.ForeignKey(Movie,on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now=True)
    return_date   = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('rent')

    def __unicode__(self):
        translation.activate('en')
        display_rent = self.customer.user.username + ' has rent ' + self.movies.title
        return display_rent
