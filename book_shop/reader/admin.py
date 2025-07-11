from django.contrib import admin
from .models import Reader

# Register your models here.

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')



