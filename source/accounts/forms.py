from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, label='Имя пользователя')
    email = forms.CharField(max_length=30, required=True, label='Почта')
    first_name = forms.CharField(max_length=150, required=True, label='Имя')
    last_name = forms.CharField(max_length=150, required=True, label='Фамилия')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    # def clean(self):
    #     super(MyUserCreationForm, self).clean()
    #     if not self.cleaned_data.get('first_name') and not self.cleaned_data.get('last_name'):
    #         raise ValidationError('Укажите свое имя и фамилию')
