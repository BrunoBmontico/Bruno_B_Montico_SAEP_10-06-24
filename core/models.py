from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    nome_turma = models.CharField(verbose_name='Turma', max_length=99, null=True, blank=True)
    nome_professor = models.CharField(verbose_name='Nome Professor', max_length=99, null=True, blank=True)
    id_professor = models.ForeignKey(User, verbose_name='Id-Professor', on_delete=models.CASCADE, null=True, blank=True)

class Atividade(models.Model):
    nome_atividade = models.CharField(verbose_name='Atividade', max_length=99, null=True, blank=True)
    id_professor = models.ForeignKey(User, verbose_name='Id-Professor', on_delete=models.CASCADE, null=True, blank=True )
    nome_professor = models.CharField(verbose_name='Nome Professor', max_length=99, null=True, blank=True)
    id_turma = models.ForeignKey(Turma, verbose_name='Id-Turma', on_delete=models.PROTECT, null=True, blank=True)
    nome_turma = models.CharField(verbose_name='Nome Professor', max_length=99, null=True, blank=True)
