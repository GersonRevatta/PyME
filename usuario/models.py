from django.db import models
import hashlib
import datetime

from django.template import defaultfilters
from django.template.defaultfilters import slugify
# Create your models here.

#class ProfileUser(models.Model):

class User(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=64)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	def chekUser(checkuser):
		try:
			usuarioRegistrado = User.objects.get(username=checkuser)
			return True
		except:	
			return False
	def crear(user,password):
		s = User()
		s.usename = user
		s.password = hashlib.sha256(str(password).encode()).hexdigest()
		s.save()
		return s
	def verificarUsuario(user):
		try:
			sa = User.objects.get(username=user)

		except User.DoesNotExist:
			return False	
	def VerificaEmail(mail):
		try:
			co = User.objects.get(email=mail)		
		except User.DoesNotExist:
			return False	

	def login(user , password):
		try:
			ver =  User.objects.get(username=user)   
		except User.DoesNotExist:
			return False
		c=hashlib.sha256(str(password).encode()).hexdigest()
		if ver.password==c:            
			return True
		else:
			return False


class Category(models.Model):
	name= models.CharField(max_length=50)
	concept= models.TextField()
	def __str__(self):
		return self.name

class ProfileImage(models.Model):
	profile = models.ForeignKey(User, null=True,blank=True)
	companyimage = models.ImageField(upload_to='empresas/')
	biography = models.ImageField(upload_to='biografias')

	

class UserProfile(models.Model):
	SERVICIO = "S"
	PRODUCTO = "P"
	CATEGORIA_CHOICES = (
		(SERVICIO,"Servicio"),
		(PRODUCTO,"Producto"))
	companyname = models.CharField(max_length=100)
	companyconcept = models.TextField()
	contact = models.IntegerField()
	companyservice = models.CharField(choices=CATEGORIA_CHOICES,default=SERVICIO,max_length=3)
	user = models.ForeignKey( User , null=True , blank=True)
	category = models.ForeignKey(Category, null= True , blank=True)
	profileimage = models.ForeignKey(ProfileImage , null=True ,blank=True)
	#category = models.CharField(choices=Category.objects.all(),initial=0)
	#category = models.CharField(choices=CATEGORIA_CHOICES,default=SERVICIO,max_length=3)
	slug = models.SlugField(max_length=100)
	def save(self,*args,**kwargs):
		self.slug = slugify(self.companyname)
		super(UserProfile,self).save(*args, **kwargs)
	def checkaa(userCheck):
		try:
			hi = UserProfile.objects.get(user=userCheck)
			return True
		except UserProfile.DoesNotExist:
			return False
	def checkName(name):
		try:
			nombre = UserProfile.objects.get(companyname=name)
			return True
		except UserProfile.DoesNotExist:
			return False

