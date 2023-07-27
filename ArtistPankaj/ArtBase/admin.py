from django.contrib import admin
from ArtBase.models import *
# Register your models here.

@admin.register(paintings)
class AdminPainting(admin.ModelAdmin):
    list_display=('id','art')

@admin.register(feedback)
class Adminfeedback(admin.ModelAdmin):
    list_display=('id','name','msg')

@admin.register(book)
class AdminBook(admin.ModelAdmin):
    list_display=('id','name','num','img')

@admin.register(contact)
class AdminContact(admin.ModelAdmin):
    list_display=('id','name','num','msg')