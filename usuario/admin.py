from django.contrib import admin
from .models import Category
# Register your models here.
class AdminCategory(admin.ModelAdmin):
	fields=["name","concept"]
	list_filter = ["name"]
	list_display = ["name"]


admin.site.register(Category,AdminCategory)


