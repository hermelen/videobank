# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, MovieGenre, Actor, Movie, MovieRent, Director, Country

# Register your models here.

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user')


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug')



class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'picture')



class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'country', 'director', 'lenght', 'picture', 'release_date', 'rented', 'slug', 'synopsis', 'trailer_url')



class MovieRentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'movies', 'checkout_date', 'return_date')



class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'picture')



class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRent, MovieRentAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Country, CountryAdmin)
