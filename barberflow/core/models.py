from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=False, blank=False)

    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    
    #não obrigatorio
    complemento = models.CharField(max_length=100, blank=True, null=True)
    
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]
    estado = models.CharField(max_length=2, choices=UF_CHOICES)

    def __str__(self):
        return f"{self.nome} - {self.cidade}/{self.estado}"
    
class Barbeiro(models.Model):
    nome_barbeiro = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return self.nome_barbeiro

class Atendimento(models.Model):
    cliente_atendimento = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbeiro_atendimento = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    OPCOES_PAGAMENTO = [
        ('dinheiro', 'Dinheiro'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('pix', 'Pix'),
    ]
    tipo_pagamento = models.CharField(max_length=100, choices=OPCOES_PAGAMENTO, default='dinheiro', null=True, blank=True)
    
    OPCOES_STATUS = [
        ('aguardando', 'Aguardando'),
        ('andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado')]
    
    status = models.CharField(max_length=20, choices=OPCOES_STATUS, default='aguardando')

    def __str__(self):
        return f"Atendimento para {self.cliente_atendimento.nome} com {self.barbeiro_atendimento.nome_barbeiro} em {self.data_hora}"