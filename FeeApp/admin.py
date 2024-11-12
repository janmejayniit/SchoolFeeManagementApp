from django.contrib import admin
from .models import FeeMaster, StudentFee, FeeInvoice

# Register your models here.
class FeeMasterAdmin(admin.ModelAdmin):
    list_display=['class_id', 'fee_name','created_at']

class StudentFeeAdmin(admin.TabularInline):
    model=StudentFee

class FeeInvoiceAdmin(admin.ModelAdmin):
    list_display = ['student','payment_amount','gst_percentage','total_amount','payment_date']
    inlines = [StudentFeeAdmin]

admin.site.register(FeeMaster, FeeMasterAdmin)
admin.site.register(FeeInvoice, FeeInvoiceAdmin)
# admin.site.register(StudentFeeAdmin)

