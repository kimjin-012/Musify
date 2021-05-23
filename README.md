# Project Musify!
### Inspired by Spotify

Creating Similar Website to Spotify

## About this Project
This is a basic Web platform where the user could register/login and search a music that they wish to listen to through spotify search.
This web uses Spotify API and it allows users to use all the Spotify musics library.
User is allow to like the songs to save it also it will give you the recommendation song choice from your listening music.

### Built with
- Python
- Django
- Regex

## Getting Started
Here's how to setup virtual environment for Django and basic Django structure for web
# Django Note

## About virtual environment
- how to create
>python -m venv environment_name_here (example: pyEnv)
- activate virtual environment
> call py3Env\Scripts\activate
- deactivate virtual environment
> deactivate
- use 'pip list' to see other installed pacakges
- to install use 'pip'
> pip file_name_here
- for the Django project let's Install Django
> pip install Django==2.2.4

&nbsp;
## How to start django project
1. Go to corresponding file location where you like to begin the project
2. To begin call the django startproject 
> django-admin startproject your_project_name_here
3. Enter the project folder, many files should have been created
> cd your_project_name_here
4. Now create a app
> python manage.py startapp your_app_name_here
5. app files has been created
6. Go to project/settings.py and visit the INSTALLED_APPS
> INSTALLED_APPS = [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'your_app_name_here', <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
**there are more code here, dont delete it** <br>
]
7. Visit project/urls.py and inside the urlpatterns, call the app's urls
> from django.urls import path, include <-- the 'include' is added 
> ```
> path('', include('your_app_name_here.urls'))
> ```
8. Go to app folder and create urls.py there as well, it will look very similar to you can copy the url from the project url.py, the same import path but make sure you add the new import line, also the urlpatterns.
> from django.urls import path
<br><br>
> from . import views
```
 urlpatterns = [ <br>
 path('', views.index)<br>
 ]
```

9. visit the views.py in your app folder now, here we can call other html files and such from the path we have been given.
>from django.shortcuts import render, HttpResponse "<-- this is added" <br>
>
> def index(request): <br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return HttpResponse("anything here")

10. when everything is setup/worked you can activate the server by
>python manage.py runserver <br>
>**this is run in the main project foler, where project/app folder are in** <br>

11. To access the server that has been activated use one of the two(first recommended)
> localhost:8000 <br>
> 127.0.0.1:8000 <br>

&nbsp;&nbsp;&nbsp;&nbsp;
## Using urls
- To make route to more different web such as /ex1/ex2/ex3... we use the urls.py from the app folder.
- Just like we had def index(request) from the views.py, we will call more path
- inside the urlpatterns, path('/ex1', views.another_function_name)
> urlpatterns = [ <br>
&nbsp;&nbsp;&nbsp;&nbsp; path('', views.index)<br>
&nbsp;&nbsp;&nbsp;&nbsp; path('/word', views.function_word) <br>
&nbsp;&nbsp;&nbsp;&nbsp; path('/word/more', views.more_function_word)<br>
]
>
- rememeber that each time the function is called, the corresponding function must exist inside of the views.py file.


## Contact / About Me
Jin Kim - [Github](https://github.com/kimjin-012) - [LinkedIn](https://www.linkedin.com/in/jin-kim-code/)
