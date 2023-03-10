from django.http import HttpResponse
from django.shortcuts import  render
# from .forms import NewUserForm
# from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import TemplateView

# def register_request(request):
	

# Create your views here.


# def index(request):
#     return render(request, 'home.html')

# def second_page(request):
#     return HttpResponse("<em>Second Page!</em>")

def entrar(request):
    inject_help = {'inject_help':'Help Page (Injected from  views)'}
    return render(request, 'entrar.html', context=inject_help)

def sugerencias(request):
    my_dict = {'pagina_sugerencias':'Hello this is the sugerencias page.'}
    return render(request, 'sugerencias.html', context= my_dict)



# def signup(request):

#     form = NewUserForm()
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('Error, Form is invalid')
#     return render(request, 'templates/buscoAmigosApp/users/signup.html',{'form':form})

# # def login_page(request):
# #     return render(request, 'templates/buscoAmigosApp/users/login.html')


class HomePageView(TemplateView):
    template_name = "home.html"

# class AboutPageView(TemplateView):
#     template_name = "about.html"

# class SignUpView(TemplateView):
#     template = "signup.html"