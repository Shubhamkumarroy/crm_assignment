from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('homepage/',views.homepage,name="homepage"),
    path('sendmail',views.sendmail,name="sendmail")

   
]