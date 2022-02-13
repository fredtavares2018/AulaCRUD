from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Clientes, Professores
import requests

#serve para redirecionar pagina
from django.urls import reverse_lazy


def abertura_modelform(request):
    response = requests.get('https://sistemas.ufac.br/plataforma_projetos/extensao/api/projetosmapa/?format=json')
    geodata = response.json()
    return render(request, 'index.html', {
        'ip': geodata[0]['id'],
        'country': geodata[0]['areatematica']
    })


# pagina cadastro - C
class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome','email','telefone'] 
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

# pagina listagem - R     
class ClientesListagem(ListView):
    model = Clientes
    template_name = 'cadastros/listar_cadastros.html'

# pagina editar - U  
class ClientesUpdate(UpdateView):
    model = Clientes
    fields = ['nome','email','telefone']  
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

#pagina deletar - D
class ClientesDelete(DeleteView):
    model = Clientes
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('listagem')
    
    
    
# pagina cadastro - C
class ProfessoresCad(CreateView):
    model = Professores
    fields = ['nomeProfessor','emailProfessor'] 
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagemP')

# pagina listagem - R     
class ProfessoresListagem(ListView):
    model = Professores
    template_name = 'cadastros/listar_cadastros.html'
    
    
    
