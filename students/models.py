from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
