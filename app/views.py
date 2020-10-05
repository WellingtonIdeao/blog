# Create your views here.
from django.shortcuts import render, redirect
from django.forms import ModelForm
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
    return render(request, template_name, {})


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

