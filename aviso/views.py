from django.shortcuts import render
from django.http import HttpResponse
from .form import FormularioPost
from .models import Post
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse


# Create your views here.
def post(request):
	publico = Post.objects.all()	
	context = {"publico":publico}
	return render(request,"ofertas.html",context)

def postDetail(request,slug):
	producto = Post.objects.get(slug=slug)
	context = {"producto":producto}
	return render(request,"ofertaDetalle.html",context)


