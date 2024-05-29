from django.forms import ModelForm
from .models import StudentProfile

class StudentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'