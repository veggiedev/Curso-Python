from django.urls import path
from users import views
# from buscoAmigosApp.views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path('login_page/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]