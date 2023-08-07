from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
     class Meta:
         model = StudentModel
        #  fields =['name','roll']
         fields = "__all__"
        #  exclude =['roll']
         
         labels = {
             'name':'student_name',
             'roll':'student_roll'
             
         }
         
         widgets ={
            #  'name' :forms.TextInput(attrs={'class':'btn btn-primary'}),
            #  'roll':forms.PasswordInput()
         }
         help_texts ={
             'name':'write your full name'
         }