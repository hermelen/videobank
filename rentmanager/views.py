# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse

from django.http import HttpResponse

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView,  InlineFormSetFactory
from extra_views.generic import GenericInlineFormSetFactory, GenericInlineFormSet

from .models import Movie, Actor, Director, Country, MovieGenre

from .forms import ActorForm, MovieForm

# Create your views here.

class MovieListView(ListView):
    model = Movie



class MovieDetailView(DetailView):
    model = Movie


# class ActorCreateView(CreateView):
#     model = Actor
#     fields = "__all__"



class ActorsInline(InlineFormSetFactory):
    # model = Movie.actors.through
    model = Actor
    fields = ['__all__']



class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    model = Movie
    fields = "__all__"
    permission_required = 'app.change_movie'

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])



    # def form_valid(self, request, form_class):
    #     first_name_0 = request.POST.get('form-0-first_name')
    #     last_name_0  = request.POST.get('form-0-last_name')
    #     picture_0 = request.POST.get('form-0-picture')
    #     actor_0 = Actor.objects.create(first_name=first_name_0, last_name=last_name_0, picture=picture_0)
    #     context = self.get_context_data()
    #
    #     if form_class.is_valid():
    #         self.object.add(actor_0)
    #
    #     return super(ProfileFamilyMemberCreate, self).form_valid(form)

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm

    def form_valid(self, request, *args, **kwargs):
        first_name_0 = request.POST.get('form-0-first_name')
        last_name_0  = request.POST.get('form-0-last_name')
        picture_0 = request.POST.get('form-0-picture')
        actor_0 = Actor.objects.create(first_name=first_name_0, last_name=last_name_0, picture=picture_0)

        movieData = form.save(commit=False)
        movieData.actors.add(actor_0)
        movieData.save()

        return CreateView.post(self, request, args, kwargs)


    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])
