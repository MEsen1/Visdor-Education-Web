from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display =['name','phone_number','email','message']
    list_filter = ('name',)
    search_fields = ('name__startswith',)



admin.site.register(Contact,ContactAdmin)