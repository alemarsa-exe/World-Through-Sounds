from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signUp, name = 'signup'),
    path('change/', views.change, name = 'change'),
    path('contacto/', views.contacto, name = 'contacto'),
    path('descarga/', views.descarga, name = 'descarga'),
    path('index/', views.index, name = 'index'),
    path('leaderboards/', views.leaderboards, name = 'leaderboards'),
    path('login/', views.loginUser, name = 'login'),
    path('signupuser/', views.signupUser, name = 'signup'),
    path('loginunity/', views.loginUnity, name = 'loginUnity'),
    path('levelplayed/', views.levelPlayed, name = 'levelPlayed'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('dash/', views.dashboard, name = 'dashboard'),

]