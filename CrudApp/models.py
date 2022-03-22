from django.core.validators import RegexValidator
from django.db import models


class course(models.Model):
    course = models.CharField(max_length=20)

    def __str__(self):
        self.course


gender_choice = (
    ("Male", "male"),
    ("Female", "female"),
    ("Other", "other")
)


class std(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=False, unique=True)
    phno = models.IntegerField(validators=[RegexValidator(r'^[0-9]{10}$')])
    gender = models.CharField(max_length=6, choices=gender_choice, blank=False, default='Male')
    course = models.ForeignKey(course, on_delete=models.CASCADE, default='BCA')

