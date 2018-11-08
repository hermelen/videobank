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

from rentmanager.views import MovieListView, MovieDetailView, MovieUpdateView, MovieCreateView
from rentmanager.views import ActorCreateView

# from userena import views as userena_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^actor/create/', ActorCreateView.as_view(), name='actor-create'),

    url(r'^movie/create/', MovieCreateView.as_view(), name='movie-create'),
    url(r'^movie/(?P<slug>[-\w]+)/edit/$', MovieUpdateView.as_view(), name="movie-update"),
    url(r'^movie/(?P<slug>[-\w]+)/$', MovieDetailView.as_view(), name='movie-detail'),

    url(r'^accounts/', include('userena.urls')),

    url(r'^$', MovieListView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
