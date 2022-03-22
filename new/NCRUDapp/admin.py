from django.contrib import admin
from .models import student, course

admin.site.register(course)
admin.site.register(student)
