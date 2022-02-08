from django.db import models

class Clientes(models.Model):
    nome = models.CharField('Digite seu nome', max_length=200 )
    email = models.CharField('Digite seu email', max_length=200 )
    telefone = models.CharField('Digite seu telefone', max_length=15 )
    status   = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
class Professores(models.Model):
    nomeProfessor = models.CharField('Digite seu professor', max_length=200 )
    emailProfessor = models.CharField('Digite seu email professor', max_length=200 )
    status   = models.IntegerField(default=1)

    def __str__(self):
        return self.nomeProfessor