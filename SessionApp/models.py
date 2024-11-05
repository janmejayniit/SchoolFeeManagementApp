from django.db import models
from StudentApp.models import Student
from ClassApp.models import ClassMaster

# Create your models here.
class SessionMaster(models.Model):
    session_year = models.CharField(max_length=20)
    current_session = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.session_year


class StudentSession(models.Model):
    class Meta:
        unique_together = ['session','class_id','student']

    session = models.ForeignKey(SessionMaster, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassMaster, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

