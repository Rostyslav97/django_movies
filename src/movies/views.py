# from django.shortcuts import render
from movies.models import Movie
from django.views.generic import ListView, DetailView

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"

# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})

# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, "movies/movie_detail.html", {"movie": movie})