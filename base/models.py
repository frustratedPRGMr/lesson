from django.db import models

# Create your models here.
class StudentProfile(models.Model):
    name = models.CharField(max_length = 200)
    course = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
