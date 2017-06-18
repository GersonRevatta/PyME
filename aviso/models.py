from django.db import models

# Create your models here.
from django.template import defaultfilters
from django.template.defaultfilters import slugify

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.title)
		super(Post, self).save(*args, **kwargs)

#class PostDetail(models.Model):

#class Categoria():
