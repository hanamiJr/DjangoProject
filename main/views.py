from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'tittle': 'Home',
        'content': 'Главная страница магазина - Home'   
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')