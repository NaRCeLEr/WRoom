from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import *
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import authenticate
from .models import *


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
        posts.append(Post.objects.get(user=i))
    context = {
        'posts': posts,
        'username': username,
        'title': 'home'
    }
    return render(request, 'main/index.html', context=context)

# Create your views here.
def change(request):
    form = ChangeForm(request.POST)

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

