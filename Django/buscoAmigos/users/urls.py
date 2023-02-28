from django.urls import path
from users import views
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', views.login, name='login'),

]