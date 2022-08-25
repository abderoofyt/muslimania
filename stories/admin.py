from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher

@admin.register(Book)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]

@admin.register(Author)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Author._meta.fields]

@admin.register(Publisher)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Publisher._meta.fields]