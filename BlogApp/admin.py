from django.contrib import admin
from .models import *

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag)
