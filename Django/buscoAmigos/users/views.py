from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import random
# Create your views here.

from .forms import NewUserForm, UserProfileForm, login_form


def index(request):
    return render(request, 'home.html')

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        user_profile = UserProfileForm(data=request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile.save(commit=False)
            profile.user = user 
            registered = True
        else:
            print('Error, Form is invalid')
    else:
        user_form = NewUserForm()
        user_profile = UserProfileForm()
    return render(request, 'signup.html',
                  {'user_form':user_form,
                  'user_profile':user_profile,
                  'regiusterd':registered})


def about(request):
    return render(request, 'about.html')    


def login_page(request):
    return render(request, 'login.html', {'login_form':login_form})

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


def rand_prof_pic(request):
    rand_photo = (f'/templates/buscoAmigosApp/Images/{random.randint(1, 2031)}.jpg')
    return render(request, 'home.html',{'rand_photo':rand_photo})