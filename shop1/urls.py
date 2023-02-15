from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('countsss/', views.count, name='count'),
    path('wordcount/', views.wordcount, name='wordcount'),

]
