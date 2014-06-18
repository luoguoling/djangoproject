from django.db import models
from django.contrib import admin
class login1(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

admin.site.register(login1)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('username','password')

# Create your models here.
