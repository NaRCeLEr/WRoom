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
        'posts': posts,
        'username': username,
        'title': 'home'
    }
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
        user.image = request.FILES.get('new_image')
        user.username = new_username if new_username else user.username
        user.bio = new_bio if new_bio else user.bio
        user.email = new_email if new_email else user.email
        user.phone = new_phone if new_phone else user.phone
        user.save()

        return redirect('home')

    return render(request, 'main/profileedit.html', {'form': form})


def profile(request):
    user = request.user
    posts = Post.objects.filter(user=request.user)
    context = {
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
        post = Post(title=context['title'], text=context['text'], user=context['user'], cat_id=1, image = context['image'] if context['image'] else None)
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
