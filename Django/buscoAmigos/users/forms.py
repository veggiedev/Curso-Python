# from django import forms
from django.contrib.auth.forms import forms
# from django.contrib.auth.models import User
from .models import User

# Create your forms here.

class NewUserForm(forms.ModelForm):
	# email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['nombre_usuario', 'email', 'password']
		widgets = {
        'password': forms.PasswordInput(),
    }
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class login_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']

