from django import forms

from .models import User


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    full_name = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    cover = forms.ImageField(required=False)
    is_online = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'full_name',
            'image',
            'cover',
            'is_online'
        ]
