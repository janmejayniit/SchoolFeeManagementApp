from django.contrib import admin
from .models import ClassMaster

# Register your models here.
class ClassMasterAdmin(admin.ModelAdmin):
     list_display=('name','created_at')


admin.site.register(ClassMaster, ClassMasterAdmin)
