from django.db import models

# Create your models here.
GENDER_CHOICES = ( 
                    ("Male", "Male"), 
                    ("Female", "Female"), 
                    ("Other", "Other"), 
                ) 

class Student(models.Model):
    first_name = models.CharField(max_length=150, error_messages='First Name is required')
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField( max_length = 20, choices=GENDER_CHOICES, default = '1') 
    email = models.EmailField(max_length=250, unique=True, blank=False, error_messages='Email is required')
    parents_mobile = models.PositiveBigIntegerField(unique=True, error_messages='Mobile is required')
    aadhar_number = models.CharField(max_length=18, blank=False)
    address = models.TextField(max_length=2000, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    admission_date = models.DateField(blank=False, error_messages='Admission date is required')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self):
         return f'{self.first_name} {self.last_name}' 

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.profile_pic))

    image_tag.short_description = 'Image'