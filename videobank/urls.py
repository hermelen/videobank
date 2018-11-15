"""videobank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from rentmanager.views import MovieListView, RentedListView, AvailableListView
from rentmanager.views import MovieDetailView, MovieUpdateView, MovieCreateView, MovieDeleteView
from rentmanager.views import ActorCreateView, DirectorCreateView, CountryCreateView, MovieRentListView
from rentmanager.views import rent_movie, return_movie

from django.conf.urls.i18n import i18n_patterns

# from userena import views as userena_views
urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),

    url(r'^actor/create/', ActorCreateView.as_view(), name='actor-create'),
    url(r'^director/create/', DirectorCreateView.as_view(), name='director-create'),
    url(r'^country/create/', CountryCreateView.as_view(), name='country-create'),
    # movie list
    url(r'^rented/', RentedListView.as_view(), name='rented'),
    url(r'^movies$', MovieListView.as_view(), name='all'),
    # movie edit
    url(r'^movie/create/', MovieCreateView.as_view(), name='movie-create'),
    #movie detail
    url(r'^movie/(?P<slug>[-\w]+)/edit/$', MovieUpdateView.as_view(), name='movie-update'),
    url(r'^movie/(?P<slug>[-\w]+)/delete/$', MovieDeleteView.as_view(), name='movie-delete'),
    url(r'^movie/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name='movie-detail'),
    # userena
    url(r'^accounts/', include('userena.urls')),
    # rent list
    url(r'^rent/list/', MovieRentListView.as_view(), name='rentmovie-list'),
    # rent action
    url(r'^rent/(?P<slug>[-\w]+)/(?P<id>[-\w]+)/$', rent_movie, name='rent'),
    url(r'^return/(?P<slug>[-\w]+)/(?P<id>[-\w]+)/$', return_movie, name='return'),

    url(r'^$', AvailableListView.as_view(), name='availables'),
)


urlpatterns += [
    # url(r'^admin/', admin.site.urls),
    #
    # url(r'^actor/create/', ActorCreateView.as_view(), name='actor-create'),
    # url(r'^director/create/', DirectorCreateView.as_view(), name='director-create'),
    # url(r'^country/create/', CountryCreateView.as_view(), name='country-create'),
    # # movie list
    # url(r'^rented/', RentedListView.as_view(), name='rented'),
    # url(r'^movies$', MovieListView.as_view(), name='all'),
    # # movie edit
    # url(r'^movie/create/', MovieCreateView.as_view(), name='movie-create'),
    # #movie detail
    # url(r'^movie/(?P<slug>[-\w]+)/edit/$', MovieUpdateView.as_view(), name='movie-update'),
    # url(r'^movie/(?P<slug>[-\w]+)/delete/$', MovieDeleteView.as_view(), name='movie-delete'),
    # url(r'^movie/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name='movie-detail'),
    # # userena
    # url(r'^accounts/', include('userena.urls')),
    # # rent list
    # url(r'^rent/list/', MovieRentListView.as_view(), name='rentmovie-list'),
    # # rent action
    # url(r'^rent/(?P<slug>[-\w]+)/(?P<id>[-\w]+)/$', rent_movie, name='rent'),
    # url(r'^return/(?P<slug>[-\w]+)/(?P<id>[-\w]+)/$', return_movie, name='return'),
    #
    # url(r'^$', AvailableListView.as_view(), name='availables'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
