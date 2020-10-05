# Create your views here.
from django.shortcuts import render


def home(request, template_name='home.html'):
    return render(request, template_name, {})


def post(request, template_name='post.html'):
    return render(request, template_name, {})

