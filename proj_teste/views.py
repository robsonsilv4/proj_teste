from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def ler_do_banco(nome):
    lista_nomes = [
        {'nome': 'Robson', 'idade': 22},
        {'nome': 'Max', 'idade': 20},
        {'nome': 'Michael', 'idade': 15}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': '', 'idade': 0}


def fname(request, nome):
    result = ler_do_banco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('A pessoa não foi encontrada')


def fname_template(request, nome):
    idade = ler_do_banco(nome)['idade']
    return render(request, 'pessoa.html', {'idade': idade})
