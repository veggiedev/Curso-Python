from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

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

def about(request):
    return render(request, 'about.html')    


def login_page(request):
    return render(request, 'login.html')

def logout_page(request):
    return render(request, 'logout.html')

# def custom_login(request):
#     if request.user.is_authenticated:
#         return redirect('homepage')

#     form = AuthenticationForm() 
    
#     return render(
#         request=request,
#         template_name="users/login.html", 
#         context={'form': form}
#         )

def my_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


# class LoginView(generic.CreateView):
#     form_class = User


                                                                                      