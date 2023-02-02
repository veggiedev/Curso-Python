from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    my_dict = {'insert_me':'Hello I am from '}
    return render(request, 'buscoAmigosApp/index.html', context=my_dict)

def second_page(request):
    return HttpResponse("<em>Second Page!</em>")

def help(request):
    inject_help = {'inject_help':'Help Page (Injected from  views)'}
    return render(request, 'buscoAmigosApp/help.html', context=inject_help)