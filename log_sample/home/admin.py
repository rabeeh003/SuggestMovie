from django.contrib import admin
from .models import AddMovie

# Register your models here.
class Added(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(AddMovie,Added)
