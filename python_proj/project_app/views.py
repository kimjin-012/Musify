from django.shortcuts import render, HttpResponse, redirect
from . models import User, Song, Playlist, Liked_Song
import bcrypt
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from pprint import pprint
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.

creds = SpotifyClientCredentials(
    client_id= "67da7ffc8c384cbeb8c6d532319189e8",
    client_secret="aee6f3e9039246779bd9352e177ba189"
)
searchResults = ['','','','','','','','','','']
trackreco = [""]
genrereco = [""]
artisreco = [""]

token = creds.get_access_token()
print("token:")
print(token)
sp = spotipy.Spotify(auth=token)
print("spotipy:")
print(sp)

def homepage(request):
    return render(request, 'login.html')


def dispRegister(request):
    return render(request, 'register.html')


def dispPlaylist(request):
    user_id = request.session.get('userID')
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context = {
            'this_user': User.objects.get(id=user_id),
            'all_songs': Song.objects.all(),
            'playlist_songs': Playlist.objects.all().order_by("-created_at"),
            'liked_songs': Liked_Song.objects.all().order_by("-created_at"),
            # 'likes_songs': Liked.objects.all(),
            # 'playlist_songs': Playlist.objects.all()
        }
    return render(request, 'playlist.html', context)


def songs(request):
    return render(request, 'song.html')


def newsfeed(request):
    user_id = request.session.get('userID')
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context = {
            'this_user': User.objects.get(id=user_id),
            'all_songs': Song.objects.all(),
            'songInfo':searchResults,
            'liked_songs': Liked_Song.objects.all().order_by("-created_at"),
            # 'playlist_songs': Playlist.objects.all()
        }
    return render(request, 'newsfeed.html', context)

def musicPlayer(request):
    user_id = request.session.get('userID')
    if 'recom' not in request.session:
        request.session['recom'] = {}
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context = {
            'this_user': User.objects.get(id=user_id),
            'all_songs': Song.objects.all(),
            'songInfo':searchResults,
            'liked_songs': Liked_Song.objects.all().order_by("-created_at"),
            'recommend': request.session['recom']
            # 'playlist_songs': Playlist.objects.all()
        }
    return render(request, 'musicPlayer.html', context)


def profile(request):
    user_id = request.session.get('userID')
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context = {
            'this_user': User.objects.get(id=user_id),
            'all_songs': Song.objects.all(),
            'liked_songs': Liked_Song.objects.all()
            # 'playlist_songs': Playlist.objects.all()
        }
    return render(request, 'profile.html', context)


# actions

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dispRegister')

    hashed_pw = bcrypt.hashpw(
        request.POST['pword'].encode(), bcrypt.gensalt()).decode()
    print(hashed_pw)
    new_user = User.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'], username=request.POST['username'],
        email=request.POST['email'],
        password=hashed_pw
    )

    request.session['userID'] = new_user.id
    request.session['id'] = '2Uu4AnnMTJpevC0IrwAuOW'
    request.session['name'] = 'Bananaphone'
    request.session['album'] = 'Bananaphone'
    request.session['img'] = 'https://i.scdn.co/image/ab67616d00001e0286fc337533e9e5bbd36fbdca'
    request.session['artist'] = 'Raffi'
    request.session['duration'] = '194360'
    results = sp.search(q='Bananaphone', type='track', limit=10)
    for i, t in enumerate(results['tracks']['items']):
        result = t
        searchResults[i] = result
    return redirect('/musicPlayer')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    existing_user = User.objects.filter(
        username=request.POST['username']
    ).first()
    if existing_user is not None:
        if bcrypt.checkpw(request.POST['password'].encode(), existing_user.password.encode()):
            request.session['userID'] = existing_user.id
            request.session['id'] = '2Uu4AnnMTJpevC0IrwAuOW'
            request.session['name'] = 'Bananaphone'
            request.session['album'] = 'Bananaphone'
            request.session['img'] = 'https://i.scdn.co/image/ab67616d00001e0286fc337533e9e5bbd36fbdca'
            request.session['artist'] = 'Raffi'
            request.session['duration'] = '194360'
            results = sp.search(q='Bananaphone', type='track', limit=10)
            for i, t in enumerate(results['tracks']['items']):
                result = t
                searchResults[i] = result
            return redirect('/musicPlayer')
        else:
            messages.error(request, "Username or password invalid")
            return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def createSong(request):
    new_song = Song.objects.create(
        artist=request.POST['artist'], song=request.POST['song'], album=request.POST['album'], duration=request.POST['duration'])
    return redirect('/playlist')

def search(request):
    print("token:")
    print(token)
    print("spotipy:")
    print(sp)
    print(("*")*80)
    print(request.POST)
    if (len(request.POST['search']) < 1):
        return ('/musicPlayer')

    search = str(request.POST['search'])
    requestedType = str(request.POST['type'])

    if requestedType == 'track': 
        results = sp.search(q=search, type='track', limit=10)
        request.session['results'] = results
        # print(results)
        for i, t in enumerate(results['tracks']['items']):
            print(' ', i, t['name'], t['preview_url'], t['id'], t['href'], t['album']['images'][1]['url'], t['album']['name'], t['album']['uri'])

            # request.session['name'] = t['name']
            # request.session['id'] = t['id']
            # request.session['clip'] = t['preview_url']
            # request.session['song'] = t['href']
            # request.session['album'] = t['album']['name']
            # request.session['playlist'] = t['album']['uri']
            # request.session['img'] = t['album']['images'][1]['url']
            # request.session['duration'] = t['duration_ms']
            urn = 'spotify:track:'+ t['id']
            result = t
            searchResults[i] = result
        track = sp.track(urn)
        pprint(track)

        request.session['id'] = searchResults[0]['id']
        request.session['name'] = searchResults[0]['name']
        request.session['album'] = searchResults[0]['album']['name']
        request.session['img'] = searchResults[0]['album']['images'][1]['url']
        request.session['artist'] = searchResults[0]['artists'][0]['name']

    if requestedType == 'artist': #Populate top 10 songs from artist?
        results = sp.search(q=search, type='artist', limit=1)
        request.session['results'] = results
        # print(results)
        for i, t in enumerate(results['artists']['items']):
            print(' ', i, t['name'], t['id'])
            request.session['name'] = t['name']
            request.session['id'] = t['id']

        topArtistsSongs = sp.artist_top_tracks(request.session['id'], country='US')
        # print(topArtistsSongs['tracks'][0]) #This line alone prints out the same thing as a single track from the track requested line. WE CAN DO THIS!!!!
        searchResults[0] = topArtistsSongs['tracks'][0]
        searchResults[1] = topArtistsSongs['tracks'][1]
        searchResults[2] = topArtistsSongs['tracks'][2]
        searchResults[3] = topArtistsSongs['tracks'][3]
        searchResults[4] = topArtistsSongs['tracks'][4]
        searchResults[5] = topArtistsSongs['tracks'][5]
        searchResults[6] = topArtistsSongs['tracks'][6]
        searchResults[7] = topArtistsSongs['tracks'][7]
        searchResults[8] = topArtistsSongs['tracks'][8]
        searchResults[9] = topArtistsSongs['tracks'][9]

        request.session['id'] = searchResults[0]['id']
        request.session['name'] = searchResults[0]['name']
        request.session['album'] = searchResults[0]['album']['name']
        request.session['img'] = searchResults[0]['album']['images'][1]['url']
        request.session['artist'] = searchResults[0]['artists'][0]['name']

    return redirect('/musicPlayer')

def playSong(request):
    song = request.POST['button']
    playSong = sp.track(song, market='US')
    print(playSong['album']['images'][1]['url'])

    artistGenrePt1 = playSong['artists'][0]['id']
    artistGenrePt2 = sp.artist(artistGenrePt1)
    trackreco[0] = ('spotify:track:' + song)
    genrereco[0] = ('spotify:genre:' + artistGenrePt2['genres'][0])
    artisreco[0] = ('spotify:artist:' + playSong['artists'][0]['id'])
    
    print('*********************************these lists')
    print(trackreco)
    print(genrereco)
    print(artisreco)
    
    recom = sp.recommendations(seed_artists=artisreco, seed_genres=genrereco, seed_tracks=trackreco, limit=3, country='US')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$HERE IS THE RECOMMENDATIAON!')
    print(recom)
    print(recom['tracks'][0]['artists'][0]['name'])
    print(recom['tracks'][0]['id'])
    
    request.session['recom'] = recom
    
    request.session['id'] = playSong['id']
    request.session['name'] = playSong['name']
    request.session['album'] = playSong['album']['name']
    request.session['img'] = playSong['album']['images'][1]['url']
    request.session['artist'] = playSong['artists'][0]['name']
    request.session['duration'] = playSong['duration_ms']
    playedSongs = Playlist.objects.create(
        songId = request.session['id'],
        artist=request.session['artist'],
        song=request.session['name'],
        album=request.session['album'],
        duration=request.session['duration'],
        user=User.objects.get(id=(request.session['userID'])),
    )
    # print (playSong)
    return redirect('/musicPlayer')

def likeButton(request):
    song = request.POST['like-btn']
    likeSong = sp.track(song, market='US')
    
    request.session['id'] = likeSong['id']
    request.session['name'] = likeSong['name']
    request.session['album'] = likeSong['album']['name']
    request.session['img'] = likeSong['album']['images'][1]['url']
    request.session['artist'] = likeSong['artists'][0]['name']
    request.session['duration'] = likeSong['duration_ms']
    likedSongs = Liked_Song.objects.create(
        songId = request.session['id'],
        artist=request.session['artist'],
        song=request.session['name'],
        album=request.session['album'],
        duration=request.session['duration'],
        user=User.objects.get(id=(request.session['userID']))
    )
    return redirect('/musicPlayer')