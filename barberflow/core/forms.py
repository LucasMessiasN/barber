from django import forms
from .models import Cliente, Barbeiro, Atendimento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class BarbeiroForm(forms.ModelForm):
    class Meta:
        model = Barbeiro
        fields = ['nome_barbeiro', 'email', 'telefone']

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['cliente_atendimento', 'barbeiro_atendimento', 'data_hora']

        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }