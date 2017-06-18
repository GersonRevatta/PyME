
from django import forms
from .models import User , UserProfile , ProfileImage

class FormularioUsuario(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email","password"]

		#para testear :D
		#fields = "__all__"
		widgets = {
			"password":forms.TextInput(attrs={"type":"password"})

		}


class FormularioPerfil(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["companyname","companyconcept","contact","companyservice"]


class FormularioImagen(forms.ModelForm):
	class Meta:
		model = ProfileImage
		fields = ["companyimage","biography"]
		widgets = {
				'companyimage' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png'}),
				'biography' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png'}),
		}

		