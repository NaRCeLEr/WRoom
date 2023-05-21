from typing import Any, Dict
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView
from .forms import *
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import authenticate
from .models import *
import json
from chatapp.models import *
from django.db.models import Q

from users.models import User as USER


class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'main/register.html'

    def get_success_url(self):
        return reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class Authenticate(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def home(request):
    username = request.user.username
    friends = User.objects.filter(friends = request.user)
    a = []
    for i in friends:
        a.append(i.pk)
    posts = []
    for i in a:
        x = Post.objects.filter(user=i)
        for c in x:
            posts.append(c)

    context = {
        'ischeked': request.POST.get('check'),
        'posts': posts,
        'username': username,
        'title': 'home'
    }
    if request.POST.get('check'):
        print(request.POST)
        name = request.POST.get('name')
        

    return render(request, 'main/index.html', context=context)


def post_edit(request, pk):
    form = posteditForm(request.POST)
    post = Post.objects.get(pk=pk)

    if form.is_valid():
        post.title = form.cleaned_data.get('new_title') if form.cleaned_data.get('new_title') else post.title
        post.title = form.cleaned_data.get('new_image') if form.cleaned_data.get('new_image') else post.title
        post.title = form.cleaned_data.get('new_text') if form.cleaned_data.get('new_text') else post.title
        post.save()
         
        return redirect('home')

 
    context = {
            'form': form,
            'post': post
        }

    return render(request, 'main/postedit.html', context=context)




def change(request):
    form = ChangeForm(request.POST, request.FILES)

    if form.is_valid():
        username = request.user.username
        bio = request.user.bio
        email = request.user.email
        phone = request.user.phone
        new_username = form.cleaned_data.get('new_username')
        new_bio = form.cleaned_data.get('new_bio')
        new_email = form.cleaned_data.get('new_email')
        new_phone = form.cleaned_data.get('new_phone')
        user = User.objects.get(username=username)
        user.image = request.FILES.get('new_image') if request.FILES.get('new_image') else user.image
        user.username = new_username if new_username else user.username
        user.bio = new_bio if new_bio else user.bio
        user.email = new_email if new_email else user.email
        user.phone = new_phone if new_phone else user.phone
        user.save()

        return redirect('home')

    return render(request, 'main/profileedit.html', {'form': form})


def profile(request, pk):
    user = USER.objects.get(pk=pk)
    posts = Post.objects.filter(user=user)
    friends = USER.objects.filter(friends=user)
    context = {
        'friends': friends,
        'posts': posts,
        'user': user,
        'title': profile
    }
    return render(request, 'main/profile.html', context=context)


def logout_user(requset):
    logout(requset)
    return redirect('login')


class Search(ListView):
    model = USER
    template_name = 'main/friends_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = USER.objects.exclude(friends = self.request.user).values()
        context['qs_json'] = json.dumps(list(a), default=str)
        context['pos'] = self.request.POST
        return context
    

def PostV(request):
      form = PostF(request.POST, request.FILES)
      context = {
          'user': request.user,
          'title': request.POST.get('title'),
          'text': request.POST.get('text'),
          'image': request.FILES.get('image')
      }
      form = PostF(context)
      if form.is_valid():
        post = Post(title=context['title'], text=context['text'], user=context['user'], image = context['image'] if context['image'] else None)
        post.save()
        return redirect('home')
      return render(request, 'main/createpost.html', {'form': form})


def addFriend(request):

    a = request.POST.get('username')
    if a != '':
        user = request.user
        user2 = USER.objects.get(username=a)
        user.friends.add(user2)
        user2.friends.add(user)
        return redirect('home')

    return render(request, 'main/friends_search.html', {'pos': a})


# def homechat(request):
#     if request.method == 'POST':
#         try:
#             get_room = Room.get(user1=request.user)
#             return redirect('room', room='test')
        
#         except Room.DoesNotExist:
#             new_room = Room.objects.create(room_name = 'room', user1=request.user, user2=request.POST.get('name'))
#             new_room.save()
#             return redirect('room', room=new_room.room_name)
#     a = request.POST.get('name')
#     if a:
#         return render(request, 'main/login.html')

#     return render(request, 'main/login.html')

def homechat(request):
    if request.method == 'POST':
        username = list(request.POST)[1]
        other_user = User.objects.get(username=username)
        current_user = request.user

        rooms = Room.objects.filter((Q(user1 = other_user) & Q(user2 = current_user)) | (Q(user1=current_user) & Q(user2 = other_user)))
        if rooms.exists():
            room = rooms.first()
            return redirect('room', room=room.pk, user=other_user)
        else:
            room = Room.objects.create(room_name='room', user1=current_user, user2=other_user)
            room.save()
            return redirect('room', room=room.pk, user=other_user)
    return render(request, 'chatapp/index.html')



def MessageView(request, room, user):
    username = request.user.username

    room = Room.objects.get(pk=room)
    if request.method == 'POST':
        message = request.POST['message']
        print(message)
        new_message = Message(room=room, sender=username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=room)
    
    context = {
        "messages": get_messages,
        "user": username,
        'reciever': user
    }
    return render(request, 'chatapp/message.html', context=context)


class AddComment(View):
    def post(self, request, pk):
        context = {
            'user': request.user,
            'post': pk,
            'text': request.POST.get('comment-text')
        }
        if context:
            comm = Comments(user=context['user'], post_id=context['post'], text=context['text'])
            comm.save()

        return redirect('home')
