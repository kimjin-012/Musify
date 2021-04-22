from django.db import models
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = 'First name too short foo, fix it'
        if len(postData['lname']) < 2:
            errors['lname'] = 'Last name too short foo, fix it'
        if len(postData['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters long'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email too short foo, fix it'
        if User.objects.filter(email=postData['email']):
            errors['email'] = 'This email is already in use'
        if len(postData['pword']) < 2:
            errors['pword'] = 'Password too short foo, fix it'
        if postData['pword'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords dont match, try again!"
        return errors

    def login_validator(self, postData):
        errors = {}
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = 'Email too short foo, fix it'
        if not User.objects.filter(username=postData['username']):
            errors['email'] = 'Username or password is invalid'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50, default=True)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Song(models.Model):
    songId = models.CharField(max_length=200, default=True)
    artist = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration = models.IntegerField()
    # users = models.ManyToManyField(User, related_name="songs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Playlist(models.Model):
    songId = models.CharField(max_length=200, default=True)
    artist = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration = models.IntegerField()
    user = models.ForeignKey(
        User, related_name="playlists", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Liked_Song(models.Model):
    songId = models.CharField(max_length=200, default=True)
    artist = models.CharField(max_length=200)
    song = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration = models.IntegerField()
    user = models.ForeignKey(
        User, related_name="liked_songs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




def __str__(self):
    s = '\n'
    s += f'first_name: {self.first_name}\n'
    s += f'last_name: {self.last_name}\n'
    s += f'email: {self.email}\n'
    s += f'password: {self.password}\n'
    return s


