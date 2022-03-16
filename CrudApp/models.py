from django.core.validators import RegexValidator
from django.db import models


class course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


gender_choice = (
    ("Male", "male"),
    ("Female", "female"),
    ("Other", "other")
)


class std(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=False, unique=True)
    gender = models.CharField(max_length=6, choices=gender_choice, default='Male')
    course = models.ForeignKey(course, on_delete=models.CASCADE, default='BCA')
    phno = models.IntegerField(validators=[RegexValidator(r'^[0-9]{10}$')])
