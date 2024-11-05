from django.contrib import admin
from .models import SessionMaster, StudentSession

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    list_display=('session_year','is_active')

class StudentSessionAdmin(admin.ModelAdmin):
    list_display=( 'session','class_id','student')

admin.site.register(SessionMaster, SessionAdmin)
admin.site.register(StudentSession, StudentSessionAdmin)