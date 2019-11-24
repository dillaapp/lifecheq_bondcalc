from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('bondinfo_save', views.bondinfo_save, name="bondinfo_save"),
    path('get', views.get, name="get"),
    path('backtoregester', views.backtoregester, name="backtoregester"),
 

    
]