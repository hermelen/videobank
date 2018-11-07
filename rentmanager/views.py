# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils.decorators import method_decorator #decorator
from django.views.decorators.csrf import csrf_exempt #decorator

from django.urls import reverse

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView,  InlineFormSetFactory
from extra_views.generic import GenericInlineFormSetFactory, GenericInlineFormSet

from .models import Movie, Actor, Director, Country, MovieGenre

from .forms import ActorForm, MovieForm

from django.db.models import Q

from django.template import loader

# Create your views here.

class MovieListView(ListView):
    model = Movie



class MovieDetailView(DetailView):
    model = Movie


# class ActorCreateView(CreateView):
#     model = Actor
#     fields = "__all__"


@method_decorator(csrf_exempt, name = 'dispatch')
class ActorCreateView(CreateView):
    model = Actor
    form_class = ActorForm
    # fields = '__all__'

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
        queryset = Actor.objects.filter( Q(first_name=post_first_name) & Q(last_name=post_last_name) )
        print(queryset)
        for actor in queryset:
            return JsonResponse({
                "first_name" : actor.first_name,
                "last_name" :  actor.last_name,
                "pk":          actor.pk
            })
        # template = loader.get_template("movie_form.html")
        # return HttpResponse(template.render())

    def get_success_url(self):
        return reverse("movie-create")




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
    # fields = "__all__"
    form_class = MovieForm
    # template_name = 'rentmanager/movie_form.html'
    # success_url = '/'
    # inlines = [ActorCreateView,]

    # fields = "__all__"

    # def form_valid(self, request, *args, **kwargs):
    #     first_name_0 = request.POST.get('form-0-first_name')
    #     last_name_0  = request.POST.get('form-0-last_name')
    #     picture_0 = request.POST.get('form-0-picture')
    #     actor_0 = Actor.objects.create(first_name=first_name_0, last_name=last_name_0, picture=picture_0)
    #
    #     movieData = form.save(commit=False)
    #     movieData.actors.add(actor_0)
    #     movieData.save()
    #
    #     return CreateView.post(self, request, args, kwargs)


    def get_success_url(self):
        return reverse("movie-detail", args=[self.object.slug])
