from django.forms import ModelForm, formset_factory
from .models import Actor, Director, Movie



class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"



class MovieForm(ModelForm):
    ActorFormset = formset_factory(ActorForm, extra=3)
    class Meta:
        model = Movie
        fields = "__all__"

#
#
#
# class DirectorForm(ModelForm):
#     class Meta:
#         model = Director
#         fields = "__all__"
