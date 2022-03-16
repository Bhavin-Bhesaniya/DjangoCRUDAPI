from django.forms import ModelForm
from .models import std


class myForm(ModelForm):
    class Meta:
        model = std
        fields = '__all__'
