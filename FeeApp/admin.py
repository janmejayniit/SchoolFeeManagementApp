from django.contrib import admin
from .models import FeeMaster, StudentFee

# Register your models here.
class FeeMasterAdmin(admin.ModelAdmin):
    list_display=['class_id', 'fee_name','created_at']

class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ['student','fee','amount']

admin.site.register(FeeMaster, FeeMasterAdmin)
admin.site.register(StudentFee, StudentFeeAdmin)

