# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

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

from .models import Movie, Actor, Director, Country, MovieGenre, MovieRent, Customer

from .forms import ActorForm, MovieForm

from django.db.models import Q

from django.template import loader

# Create your views here.
class RentedListView(ListView):
    model = Movie

    def get_queryset(self):
        queryset = Movie.objects.filter(rented = True)
        return queryset



class MovieListView(ListView):
    model = Movie



class MovieDetailView(DetailView):
    model = Movie



@method_decorator(csrf_exempt, name = 'dispatch')
class ActorCreateView(CreateView):
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
        print(queryset)
        return JsonResponse({
            "first_name" : queryset.first_name,
            "last_name" :  queryset.last_name,
            "pk":          queryset.pk
        })

    def get_success_url(self):
        return reverse("movie-create")




class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    model = Movie
    fields = "__all__"
    permission_required = 'movie.change_movie'

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])



class MovieCreateView(CreateWithInlinesView):
    model = Movie
    form_class = MovieForm

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])



def rent_movie(request, slug, id):
    model = MovieRent
    movie = Movie.objects.get(slug=slug)
    customer = Customer.objects.get(id=id)

    movie.rented = True
    movie.save()

    new_rent = MovieRent(movies=movie, customer=customer)
    new_rent.save()
    return redirect("userena_profile_detail", username=customer.user.username)
