from django import forms
from aviso.models import Post



class FormularioPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","description"]

