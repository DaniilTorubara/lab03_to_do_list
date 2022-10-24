from dataclasses import field
from django.forms import ModelForm
from.models import TODO

class ToDoForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'description', 'important_check']