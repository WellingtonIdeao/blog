from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('post', post, name='post'),
    path('form', create_user, name='form'),
    path('login', logar, name='logar'),
    path('logout', deslogar, name='deslogar')
]