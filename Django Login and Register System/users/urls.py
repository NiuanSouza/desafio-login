from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('menu/', views.menu, name="menu"),

]
