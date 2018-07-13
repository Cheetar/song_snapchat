from django.urls import path, register_converter

from . import converters, views

register_converter(converters.TokenConverter, 'token')

urlpatterns = [
    path('', views.index, name='index'),
    # Token is 32 chars long hexaecimal string
    path('profile/<token:profile_token>/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('song/<token:song_token>/', views.song, name='song'),
]
