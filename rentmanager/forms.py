from django.forms import ModelForm, formset_factory
from .models import Actor, Director, Movie, Country



class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"



class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"



class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = "__all__"



class MovieForm(ModelForm):
    ActorFormset = formset_factory(ActorForm, extra=1)
    DirectorFormset = formset_factory(DirectorForm, extra=1)
    CountryFormset = formset_factory(CountryForm, extra=1)
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
