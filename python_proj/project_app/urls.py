from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('dispRegister', views.dispRegister),
    path('playlist', views.dispPlaylist),
    path('songs', views.songs),
    path('newsfeed', views.newsfeed),
    path('musicPlayer', views.musicPlayer),
    path('profile', views.profile),


    # action
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('createSong', views.createSong),
    path('search', views.search),
    path('playSong', views.playSong),
    path('likeButton', views.likeButton),
]
