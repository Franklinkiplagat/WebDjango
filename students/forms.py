from django import forms
from students.models import StudentComplain


class StudentForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Name')
    age = forms.IntegerField(min_value=18, max_value=25, required=True, label='AGE')
    check = forms.BooleanField(required=False, label='PRESENT')
    Category = forms.ChoiceField(choices=[('Student', 'Student'), ('Other', 'Other')], required=True, label='Category')


class NewStudentComplainForm(forms.ModelForm):
    class Meta:
        model = StudentComplain
        fields = ('name', 'body')
