from django.shortcuts import render
from django.http import HttpResponse
from .form import FormularioPost
from .models import Post
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse
from usuario.models import Category


from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger
from django.db.models import Q
# Create your views here.
def post(request):
	publico = Post.objects.all()
	categoria = Category.objects.all()
	query = request.GET.get("q")
	print(query)
	if query:
		publico = publico.filter(
			Q(title__startswith=query)|
			Q(user__companyname__startswith=query)|
			Q(user__category__name__startswith=query)
			).distinct()
	paginator = Paginator(publico,20)		
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		publico = paginator.page(page)
	except PageNotAnInteger:
		publico = paginator.page(1)
	except EmptyPage:
		publico = paginator.page(paginator.num_pages)
	context = {"publico":publico,"categoria":categoria}
	return render(request,"ofertas.html",context)


'''
class Post(models.Model):
	user = models.ForeignKey(UserProfile , null=True,blank=True)
	title = models.CharField(max_length=100)
	
class Category(models.Model):
	name= models.CharField(max_length=50)
	concept= models.TextField()
	def __str__(self):
		return self.name
	

class UserProfile(models.Model):

	user = models.ForeignKey( User , null=True , blank=True)
	category = models.ForeignKey(Category, null= True , blank=True)
	profileimage = models.ForeignKey(ProfileImage , null=True ,blank=True)

'''	
def postDetail(request,slug):
	producto = Post.objects.get(slug=slug)
	
	context = {"producto":producto}
	return render(request,"ofertaDetalle.html",context)


def eliminarPost():
	...	

def editarPost():
	...
