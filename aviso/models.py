from django.db import models

# Create your models here.
from django.template import defaultfilters
from django.template.defaultfilters import slugify
from usuario.models import User , UserProfile


class PostImage(models.Model):
	title = models.CharField(max_length=100)
	imagepost = models.ImageField(upload_to='post/')


class Post(models.Model):
	user = models.ForeignKey(UserProfile , null=True,blank=True)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	precio = models.FloatField(null=True,blank=True)
	postimage = models.ForeignKey(PostImage,null=True,blank=True)
	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.title)
		super(Post, self).save(*args, **kwargs)




#class  PostType(models.Model):

#class PostDetail(models.Model):

#class Categoria():
