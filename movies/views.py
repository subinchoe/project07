from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = ReviewForm()
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)

@require_POST
def review_new(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.movie = movie
        review.save()
        return redirect('movies:detail', id)
    else:
        return redirect('movies:index')


def review_delete(request, movie_id, review_id):
    get_object_or_404(Review, id=review_id).delete()
    return redirect('movies:detail', movie_id)

def like(request, id):
    user = request.user
    movie = get_object_or_404(Movie, id=id)
    if movie.like_users.filter(id=user.id):
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect('movies:detail', id)
