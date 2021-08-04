from django.contrib import admin
from .models import ecomm_model
# Register your models here.
class ecomm_admin(admin.ModelAdmin):
    list_display = ['name','phone','email','product','quantity']

admin.site.register(ecomm_model,ecomm_admin)