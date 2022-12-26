from django.contrib import admin
from django.urls import path, include
from vin import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('verifymail', views.verifymail, name='verifymail'),
    path('infomail', views.infomail, name='infomail'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('sendmail', views.sendmail, name='sendmail'),
    path('signout', views.signout, name='signout')
]
