from django.shortcuts import render
# Create your views here.
from .form import FormularioUsuario , FormularioPerfil ,FormularioImagen
from .models import User , UserProfile , ProfileImage , Category
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

  
def landing(request):
	return render(request,"landing.html",{})

def RegistroUser(request):
	usuario=""
	if request.POST:
		frm = FormularioUsuario(request.POST)
		if frm.is_valid():
			VerificarUsuario = User.verificarUsuario(user=request.POST["username"])
			if VerificarUsuario == False:
				verEmail=User.VerificaEmail(mail=request.POST["email"])
				if verEmail == False:
					a=User.crear(user = request.POST["username"] , password = request.POST["password"])
					a.username=frm.cleaned_data["username"]
					a.email=frm.cleaned_data["email"]
					a.save()
					z = request.POST['username']
					request.session['userr']=z
					return HttpResponseRedirect(reverse('RegistroPerfil'))
				else:
					usuario ="El correo ya esta en uso , Registre otro"	
			else:
				usuario="El usuario  ya esta en uso elige otro NOmbre de usurio"
				


	else:	
		frm = FormularioUsuario()
	context = {"frm":frm,"usuario":usuario}	
	return render(request,"registro.html",context)



	#biografia
	#imagen de perfil

def registerProfile(request):
	if request.POST:
		re = FormularioPerfil(request.POST)	
		form2 = FormularioImagen(request.POST,request.FILES )
		if re.is_valid() and form2.is_valid():
			b = form2.save()
			a = re.save()
			a.user  = User.objects.get(username=request.session['userr'])
			a.companyname = re.cleaned_data["companyname"]
			a.companyconcept = re.cleaned_data["companyconcept"]
			a.contact = re.cleaned_data["contact"]
			categoria = re.cleaned_data["categoria"]			
			usuarioObjeto = User.objects.get(username=request.session['userr'])
			b.profile = usuarioObjeto
			a.save()		
			b.save()
			em = User.objects.get(username=request.session['userr'])
			empresa = UserProfile.objects.get(user= em)
			empresa.category = Category.objects.get(name=categoria)
			y = empresa.slug
			empresa.save()
			return HttpResponseRedirect(reverse("biografia",args=(y,)))
	else:		
		form2 = FormularioImagen()
		re = FormularioPerfil()
	context = {"re":re,"form2":form2}
	return render(request,"perfil.html",context)
#http://127.0.0.1:8000/bio/jajaj-es-chico-linux


def myProfile(request):
	a = User.objects.get(username=request.session["userr"])
	empresa = UserProfile.objects.get(user=a)
	return HttpResponseRedirect(reverse("biografia",args=(empresa.slug,)))


def biografia(request,slug):
	empresa = UserProfile.objects.get(slug=slug)
	user = User.objects.get(username=request.session['userr'])
	empresaimage = ProfileImage.objects.get(profile=user)
	context = {"empresa":empresa,"empresaimage":empresaimage}
	return render(request,"biografia.html",context)


def formulario(request):
	frm = FormularioRegistro()
	return render(request,'register.html',{'frm':frm})

#sesion
def login(request):
	if request.POST:
		frm = FormularioUsuario(request.POST)
		if frm.is_valid:
			rpta = User.login(user=request.POST["username"],password=request.POST["password"])
			if rpta == True:
				z = request.POST['username']
				request.session['userr']=z
				return HttpResponseRedirect(reverse("checkProfile"))
			else:
				return HttpResponseRedirect(reverse("login"))
				
	else:	
		frm = FormularioUsuario()
	context = {"frm":frm}
	return render(request,"login.html",context)
	
	

def checkProfile(request):
	a = User.objects.get(username=request.session["userr"])
	rpt = UserProfile.checkaa(userCheck=a)
	print(rpt)
	if rpt == False:
		return HttpResponseRedirect(reverse("RegistroPerfil"))
	else:
		return HttpResponseRedirect(reverse("post"))

			
	

def logout(request):
	try:
		del request.session['userr']
	except KeyError:
		pass
	return HttpResponseRedirect(reverse("landing"))
	
	

#funcionalidad
def newPost():
	...



