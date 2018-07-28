from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm


def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})


def pessoas_new(request):
    form = PessoaForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list')
    return render(request, 'pessoa_form.html', {'form': form})
