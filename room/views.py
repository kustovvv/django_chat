from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room/detail.html', {'room': room, 'messages': messages})