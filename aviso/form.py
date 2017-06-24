from django import forms
from aviso.models import Post ,PostImage




class FormularioPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","description"]

class FormularioPostImage(forms.ModelForm):
	class Meta:
		model = PostImage
		fields = ["imagepost"]