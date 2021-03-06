# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email'
        ]


def home(request, template_name='home.html'):
    post = Post.objects.all()  # testar template for para  post vazio
    return render(request, template_name, {'posts': post})


def post(request, template_name='post.html'):
    return render(request, template_name, {})


def create_user(request, template_name='user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.is_staff = False
        user.save()
        return redirect('home')
    else:
        return render(request, template_name, {'form': form})


def logar(request, template_name='login.html'):
    next = request.GET.get('next', '/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return HttpResponseRedirect(settings.LOGIN_URL)
    else:
        return render(request, template_name, {'redirect_to': next})


def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)



