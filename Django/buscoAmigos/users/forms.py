from django import forms
# from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from .models import UserProfile

# Create your forms here.

class NewUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['username', 'email', 'password']
	
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
	class UserProfile(forms.ModelForm):
		class Meta():
			model = UserProfile
			fields = ('nacimiento', 'genero', 'provincia', 'ciudad', 'disponibilidad', 'lugar_comida', 'musica', 'musica_relax', 'musica_animada', 'salir', 'actividades', 'latitud', 'longitud')






class login_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']

