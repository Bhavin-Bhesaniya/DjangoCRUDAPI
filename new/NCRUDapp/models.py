from django.core.validators import RegexValidator
from django.db import models


class course(models.Model):
    course = models.CharField(max_length=20)

    def __str__(self):
        self.course


gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=False)
    phone = models.IntegerField(validators=[RegexValidator(r'^[0-9]{10}$')])
    gender = models.CharField(max_length=20, choices=gender_choice, blank=False, default='Male')
    course = models.ForeignKey(course, on_delete=models.CASCADE, default='BCA')
