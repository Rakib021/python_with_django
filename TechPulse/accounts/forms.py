from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username', 'password1', 'password2')

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Teacher  # Can use Student if needed
