from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import TemplateView

# def register_request(request):
	

# Create your views here.


def index(request):
    my_dict = {'insert_me':'Hello I am from '}
    return render(request, 'buscoAmigosApp/index.html', context=my_dict)

def second_page(request):
    return HttpResponse("<em>Second Page!</em>")

def help(request):
    inject_help = {'inject_help':'Help Page (Injected from  views)'}
    return render(request, 'help.html', context=inject_help)

def sugerencias(request):
    my_dict = {'pagina_sugerencias':'Hello this is the sugerencias page.'}
    return render(request, 'sugerencias.html', context= my_dict)


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"