from django import forms
from .models import Professor


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ("name", "curriculum")

