from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('', views.user_list, name="user_list"),
    path('<int:id>/', views.user_detail, name="user_detail"),
]