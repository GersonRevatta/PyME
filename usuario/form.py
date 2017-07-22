
from django import forms
from .models import User , UserProfile , ProfileImage , Category

class FormularioUsuario(forms.ModelForm):
	password = forms.CharField(max_length=30,min_length=7,widget=forms.PasswordInput(),error_messages={'required':'Ingresa correctamente el password'})
	class Meta:
		model = User
		fields = ["username","email","password"]
#otra forma de hacer los widgets			
#		widgets = {
#			"password":forms.TextInput(attrs={"type":"password"})
#		}
		def clean_email(self):
			email = self.cleaned_data.get("email")
			nombre , proveedor = email.split("@")
			dominio , extencion = proveedor.split(".")
			if extencion == "com":
				raise forms.ValidationError("Escribe correctamente tu correo")
			return email	
		


class FormularioPerfil(forms.ModelForm):
	companyname = forms.CharField(max_length=30)
	categoria = forms.ModelChoiceField(queryset=Category.objects.all(),initial=0)
	companyconcept = forms.CharField(min_length=200,widget=forms.Textarea() )
	contact = forms.CharField(min_length=9, max_length=9 )
	class Meta:
		model = UserProfile
		fields = ["companyname","companyconcept","contact","companyservice"]


class FormularioImagen(forms.ModelForm):
	class Meta:
		model = ProfileImage
		fields = ["companyimage","biography"]
		widgets = {
				'companyimage' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png','required':'Necesitas una imagen para tu perfil'}),
				'biography' : forms.FileInput(attrs = {'accept': 'image/gif, image/jpeg, image/png','required':'Necesitas una imagen de biografia'}),
		}

		