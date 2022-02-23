from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('index',views.index),
  path('home_view',views.home_view),
  ]