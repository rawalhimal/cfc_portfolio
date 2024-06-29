from django.contrib import admin
from .models import Contact,Service
# Register your models here.
admin.site.site_header = "Portfolio"
admin.site.site_title = "My Personal Project"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

@admin.register(Service)
class ServiceContact(admin.ModelAdmin):
    list_display = ['id','image','title','description']