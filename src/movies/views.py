from django.shortcuts import render, redirect
from movies.models import Actor, Movie
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from movies.forms import ReviewForm

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

class ActorView(DetailView):
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"

# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})

# class MovieDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, "movies/movie_detail.html", {"movie": movie})