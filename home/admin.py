from django.contrib import admin
from .models import Contact,Teacher,Branch


class ContactAdmin(admin.ModelAdmin):
    list_display =['name','phone_number','email','message']
    list_filter = ('name',)
    search_fields = ('name__startswith',)
class TeacherAdmin(admin.ModelAdmin):
    list_display =['first_name','last_name','email_teacher','branch']
    list_filter = ('branch',)
    search_fields = ('name__startswith',)



admin.site.register(Contact,ContactAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Branch)