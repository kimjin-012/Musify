from django.urls import path
from . import views

# Url patterns for ivews.
urlpatterns = [
    path('', views.index)
]