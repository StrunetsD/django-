from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=3, required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=1, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=1, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit= True):
        user = super().save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
