from django.core.management.base import BaseCommand
from rentmanager.models import Movie
from django.utils import translation
import csv
from django.http import HttpResponse



class Command(BaseCommand):
    help = "Export an .csv file of all movie"

    def handle(self, *args, **options):
        translation.activate('en')

        movieList = Movie.objects.all()

        with open('movies.csv', 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['title', 'genre', 'actors', 'country', 'director', 'lenght', 'release_date','synopsis'])

            for movie in movieList:
                title = movie.title
                synopsis = movie.synopsis
                genre = movie.genre.label
                actorList = movie.actors.all()
                actors = ""
                for actor in actorList:
                    actors += actor.first_name.capitalize() + " " + actor.last_name.upper() + " "
                country = movie.country.name
                director = movie.director.first_name + " " + movie.director.last_name
                lenght = str(movie.lenght)
                release_date = movie.release_date.strftime("%Y-%m-%d %H:%M:%S")

                filewriter.writerow([title, genre, actors, country, director, lenght, release_date, synopsis])
