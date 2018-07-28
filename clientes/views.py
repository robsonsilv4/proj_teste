from django.shortcuts import render
from .models import Pessoa


def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})
