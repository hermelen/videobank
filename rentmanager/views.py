# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from datetime import datetime

from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator #decorator
from django.views.decorators.csrf import csrf_exempt #decorator

from django.urls import reverse

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView,  InlineFormSetFactory
from extra_views.generic import GenericInlineFormSetFactory, GenericInlineFormSet

from .models import Movie, Actor, Director, Country, MovieGenre, MovieRent, Customer, Director, Country

from .forms import ActorForm, MovieForm, DirectorForm, CountryForm

from django.db.models import Q

from django.template import loader

# Create your views here.
class RentedListView(ListView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Movie

    def get_queryset(self):
        queryset = Movie.objects.filter(rented = True)
        return queryset

class AvailableListView(ListView):
    model = Movie

    def get_queryset(self):
        queryset = Movie.objects.filter(rented = False)
        return queryset


class MovieListView(ListView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Movie



class MovieDetailView(DetailView):
    model = Movie



@method_decorator(csrf_exempt, name = 'dispatch')
class ActorCreateView(CreateView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Actor
    form_class = ActorForm

    def post(self, request, *args, **kwargs):
        post_first_name=request.POST.get("form-0-first_name")
        post_last_name = request.POST.get("form-0-last_name")
        post_picture = request.POST.get("form-0-picture")
        new_actor = Actor(
            first_name= post_first_name,
            last_name = post_last_name,
            picture   = post_picture
        )
        new_actor.save()
        queryset = Actor.objects.get( Q(first_name=post_first_name) & Q(last_name=post_last_name) )
        return JsonResponse({
            "type"       : "actor",
            "first_name" : queryset.first_name,
            "last_name"  : queryset.last_name,
            "pk"         : queryset.pk
        })

    def get_success_url(self):
        return reverse("movie-create")



@method_decorator(csrf_exempt, name = 'dispatch')
class DirectorCreateView(CreateView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Director
    form_class = DirectorForm

    def post(self, request, *args, **kwargs):
        post_first_name=request.POST.get("form-0-first_name")
        post_last_name = request.POST.get("form-0-last_name")
        post_picture = request.POST.get("form-0-picture")
        new_director = Director(
            first_name= post_first_name,
            last_name = post_last_name,
            picture   = post_picture
        )
        new_director.save()
        queryset = Director.objects.get( Q(first_name=post_first_name) & Q(last_name=post_last_name) )
        return JsonResponse({
            "type"       : "director",
            "first_name" : queryset.first_name,
            "last_name"  : queryset.last_name,
            "pk"         : queryset.pk
        })

    def get_success_url(self):
        return reverse("movie-create")



@method_decorator(csrf_exempt, name = 'dispatch')
class CountryCreateView(CreateView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Country
    form_class = CountryForm

    def post(self, request, *args, **kwargs):
        post_name=request.POST.get("form-0-name")
        new_country = Country(
            name= post_name,
        )
        new_country.save()
        queryset = Country.objects.get( name=post_name )
        return JsonResponse({
            "type" : "country",
            "name" : queryset.name,
            "pk"   : queryset.pk
        })

    def get_success_url(self):
        return reverse("movie-create")



class MovieCreateView(CreateWithInlinesView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Movie
    form_class = MovieForm

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])




class MovieUpdateView(UpdateView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])



class MovieDeleteView(DeleteView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = Movie

    def get_success_url(self):
        return reverse("all")



class MovieRentListView(ListView, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    model = MovieRent



def rent_movie(request, slug, id):
    model = MovieRent
    movie = Movie.objects.get(slug=slug)
    customer = Customer.objects.get(id=id)

    movie.rented = True
    movie.save()

    new_rent = MovieRent(movies=movie, customer=customer)
    new_rent.save()
    return redirect("userena_profile_detail", username=customer.user.username)



def return_movie(request, slug, id, PermissionRequiredMixin):
    permission_required = 'rentmanager.add_movie'
    movie = Movie.objects.get(slug=slug)
    movierent = MovieRent.objects.get(id=id)

    movie.rented = False
    movierent.return_date = datetime.now()

    movie.save()
    movierent.save()

    return redirect("rentmovie-list")
