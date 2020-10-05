# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField(null=False)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    descricao = models.TextField(null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

