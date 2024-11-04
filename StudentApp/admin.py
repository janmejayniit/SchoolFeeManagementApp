from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('image_tag','full_name', 'gender', 'parents_mobile', 'email', 'admission_date')
    readonly_fields = ('image_tag',)

admin.site.register(Student, StudentAdmin)