from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/review/new/', views.review_new, name="review_new"),
    path('<int:movie_id>/review/<int:review_id>/delete/', views.review_delete, name="review_delete"),
    path('<int:id>/like/', views.like, name="like"),
]
