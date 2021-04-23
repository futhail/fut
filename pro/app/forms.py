from django import forms
from .models import Student


class sud(forms.ModelForm):
       name = forms.CharField(label='الاسم',max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your name','style':'text-align:center;border:solid 0px white'}))
       age = forms.IntegerField(label='العمر')
       addrss = forms.CharField(label='العنوان',max_length=30)
       class Meta:
           model=Student
           fields=('name','age','addrss')

