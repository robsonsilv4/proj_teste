from django.shortcuts import render


def pessoas_list(request):
    return render(request, 'pessoa.html')
