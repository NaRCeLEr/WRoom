# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, View
# from .forms import *
# from django.contrib.auth import get_user_model, login
# from django.contrib.auth import authenticate


# class RegisterUser(CreateView):
#     form_class = UserForm
#     template_name = 'users/register.html'

#     def get_success_url(self):
#         return reverse_lazy('home')


# class Authenticate(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'users/login.html'

#     def get_success_url(self):
#         return reverse_lazy('home')



# def auth(request):
#     if request.method == 'POST':
#         print('kk')
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             print('o')
#             if user.is_active:
#                 print('ok')
#                 login(request, user)
#                 request.session['username'] = username
#                 return redirect('home')
#                 # return render(request,'dashboard_app/index.html',{'name':name.username})
#             else:
#                 print('sorry')
#                 return render(request, 'users/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             print('d')
#             return render(request, 'users/register.html', {'error_message': 'Invalid login'})

#     return render(request, 'users/index.html')

# def a(request):
#     form = AuthForm
#     return render(request, 'users/login.html', {'form':form})

# def home(request):
#     User = request.user.username
#     context = {
#         'username': User,
#         'title': 'home'
#     }
#     return render(request, 'users/index.html', context=context)

# # Create your views here.
