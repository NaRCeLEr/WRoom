from django.contrib import admin
from django.urls import path, include
from .views import *
from WayRoom import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', home, name='home'),
    path('', RegisterUser.as_view(), name='register'),
    path('login', Authenticate.as_view(), name='login'),
    path('change', change, name='change'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('logout', logout_user, name='logout'),
    path('post_edit/<int:pk>/', post_edit, name='post_edit'),
    path('search_friends', Search.as_view(), name='Search_friends'),
    path('create_post', PostV, name='create_post'),
    path('add_friend', addFriend, name='friend'),
    path('homechat', homechat, name='homechat'),
    path('room/<int:room>/<str:user>/', MessageView, name='room'),
    path('addcomment/<int:pk>/', AddComment.as_view(), name='addcomment'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)