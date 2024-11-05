from django.db import models
from ClassApp.models import ClassMaster
from StudentApp.models import Student
from SessionApp.models import SessionMaster
from django.utils import timezone

# Create your models here.
class FeeMaster(models.Model):
    class_id = models.ForeignKey(ClassMaster, on_delete=models.CASCADE)
    fee_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fee_name

class StudentFee(models.Model):
    session = models.ForeignKey(SessionMaster, default=None, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassMaster, default=None, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, default=None, on_delete=models.CASCADE)
    fee = models.ForeignKey(FeeMaster, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)


