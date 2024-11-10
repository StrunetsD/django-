from django import forms
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from honey_app.models import Honey
from user_honey.models import UserHoney


class HoneyForm(forms.ModelForm):
    name = forms.CharField(
        max_length=120,
        required=True,
    )
    price = forms.DecimalField(
        validators=[MinValueValidator(1)],
        max_digits=5,
        decimal_places=2)
    description = forms.CharField(required=True)
    image = forms.ImageField(required=False)
    class Meta:
        model = Honey
        fields = ('name', 'price', 'description','image')




class UpdateHoneyForm(forms.ModelForm):
    name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.DecimalField(
        validators=[MinValueValidator(1)],
        max_digits=5,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Honey
        fields = ('name', 'price', 'description')