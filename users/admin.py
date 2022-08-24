from django.contrib import admin

# Register your models here.
from .models import ProfileModel

@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProfileModel._meta.fields]