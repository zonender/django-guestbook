from django.contrib import admin

# Register your models here.
from .models import Comment

admin.site.register(Comment) #this will register the Comment table to the admin site and thus allowing us to modify date there