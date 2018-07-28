from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá, mundo!')


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
