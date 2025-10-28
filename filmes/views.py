from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Filme
from .forms import FilmeForm

class FilmeListView(ListView):
    model = Filme
    template_name = 'listar_filmes.html'
    context_object_name = 'filmes'
    ordering = ['titulo']
    paginate_by = 10 

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme_detalhes.html'
    context_object_name = 'filme'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'cadastro_filme.html'
    success_url = reverse_lazy('filme_list')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'cadastro_filme.html'
    success_url = reverse_lazy('filme_list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list')
