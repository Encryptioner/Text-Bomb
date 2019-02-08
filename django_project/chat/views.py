# chat/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import json


def chat_home(request):
    return render(request, 'chat/chat_home.html', {})


@login_required
def room(request, room_name):
    usr_names = User.objects.all().values_list('username')
    user_list = [u[0] for u in usr_names]

    no = len(User.objects.all())
    # no = range(no)

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'user_list': mark_safe(json.dumps(user_list)),
        'no': mark_safe(json.dumps(str(no))),
    })
