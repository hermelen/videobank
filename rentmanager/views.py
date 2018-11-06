# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse

from django.http import HttpResponse, JsonResponse

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



class ActorCreateView(PermissionRequiredMixin, CreateView):
    model = Actor
    form_class = ActorForm
    permission_required = 'rentmanager.add_actor'


    def post(self, request, **kwargs):
        CreateView.post(self, request, kwargs)
        return JsonResponse({
            # "editable_data_url" : reverse("Actor-update", args=[self.object.id, 'quantity']),
            # "del_button_data_url" : reverse("Actor-delete", args=[self.object.id]),
            "actor_first_name" : self.object.first_name,
            "actor_last_name" : self.object.last_name,
            "actor_id": self.object.id
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
    # form_class = MovieForm
    fields = "__all__"
    permission_required = 'movie.add_movie'

    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])



# class MovieCreateView(PermissionRequiredMixin, CreateView):
#     model = Movie
#     form_class = MovieForm
#     # fields = "__all__"
#     # success_url = '/'
#     permission_required = 'rentmanager.add_movie'
#
#
#     def get_success_url(self):
#         return reverse("movie-detail", args=[self.object.slug])
