# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, null=False)
    conteudo = models.TextField(null=False)
    categorias = models.ManyToManyField(Categoria)
    data_cadastro = models.DateTimeField(default=datetime.now, editable=False, null=False)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    descricao = models.TextField(null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

