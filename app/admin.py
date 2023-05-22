from django.contrib import admin
from .models import Recipie,Favorite,Comment

# Register your models here.

admin.site.register(Recipie)
admin.site.register(Favorite)
admin.site.register(Comment)
