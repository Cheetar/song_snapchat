from django.urls import path, register_converter

from . import converters, views

register_converter(converters.TokenConverter, 'token')

urlpatterns = [
    path('', views.index, name='index'),
    # Token is 32 chars long hexaecimal string
    path('snap/<token:snap_token>/', views.snap, name='snap'),
    path('snap/', views.snap, name='snap'),
    path('song/<token:song_token>/', views.song, name='song'),
]
