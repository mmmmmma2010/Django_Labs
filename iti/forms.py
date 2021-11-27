from django import forms
from django.db.models import fields
from.models import Student


class AddStudent(forms.ModelForm):
    class Meta:
        model=Student
        fields=['student_name','student_age','track']