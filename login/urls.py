from unicodedata import name
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
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
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('dashboard/profile', views.profile, name = "profile"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/exit/', views.remove_account, name="exit"),
    path('topscores/', views.topScores, name="topScores"),
    path('gettopscores/', views.getTopScore, name="getTopScore"),
    #path(r'^panel/del/?P<pk>\d+)/$', views.delete, name="delete"),

]