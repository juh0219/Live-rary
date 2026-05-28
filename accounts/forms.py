# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '학번(5자리)'}),
        error_messages={
            'unique': '이미 등록된 학번입니다.'
        }
    )
    first_name = forms.CharField(
        label="이름",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '이름'}),
    )
    email = forms.EmailField(
        label="이메일 주소",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': '이메일 주소'}),
        error_messages={
            'invalid': '올바른 이메일 형식이 아닙니다.'
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
