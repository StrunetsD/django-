from django import forms
from django.contrib.auth import get_user_model

from honey_app.models import Comment

user = get_user_model()

class AddCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea,required = False)
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
