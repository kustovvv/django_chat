from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('<str:slug>/', views.room_detail, name='detail'),
]
