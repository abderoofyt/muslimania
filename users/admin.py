from django.contrib import admin

# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]