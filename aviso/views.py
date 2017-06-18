from django.shortcuts import render
from django.http import HttpResponse
from .form import FormularioPost
from .models import Post
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse


# Create your views here.
def post(request):
	if request.POST:
		frm = FormularioPost(request.POST)
		if frm.is_valid():
			a = frm.save()
			a.title = frm.cleaned_data["title"]
			a.description = frm.cleaned_data["description"]
			a.save()
			return HttpResponseRedirect(reverse('post'))
		else:
			return HttpResponse("es un error corrigelo")	
	else:
		frm = FormularioPost()
	publico = Post.objects.all()	
	context = {"frm":frm,"publico":publico}
	return render(request,"ofertas.html",context)
