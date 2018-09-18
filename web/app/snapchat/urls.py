from django.urls import path, register_converter

from . import converters, views

register_converter(converters.TokenConverter, 'token')

urlpatterns = [
    path('', views.index, name='index'),
    # Token is 32 chars long hexadecimal string.
    path('snap/<token:snap_token>/', views.snap, name='snap'),
    path('snap/', views.snap, name='snap'),
    path('snap/add/<token:snap_token>/', views.add_snap, name='add_snap'),
    path('snap/add/', views.add_snap, name='add_snap'),
    path('snap/share/<token:snap_token>/', views.share_snap, name='share_snap'),
    path('song/add/<token:snap_token>/', views.add_song, name='add_song'),
    path('song/<token:song_token>/', views.song, name='song'),
]
