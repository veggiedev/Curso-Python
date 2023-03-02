from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import NewUserForm
from .models import User


def index(request):
    return render(request, 'home.html')

def signup (request):

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error, Form is invalid')
    return render(request, 'signup.html',{'form':form})
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "users/signup.html"

    
def login(request):
    return render(request, 'login.html')

# class LoginView(generic.CreateView):
#     form_class = User


                                                                                      