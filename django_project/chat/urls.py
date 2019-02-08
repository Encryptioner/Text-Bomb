
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('chat_home/', views.chat_home, name='chat-home'),
    re_path(r'^chat_home/chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
