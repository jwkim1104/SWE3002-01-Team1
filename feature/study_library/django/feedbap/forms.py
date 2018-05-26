from django import forms

from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('serialNum', 'userName', 'userID', 'email', 'userPW', 'phonenumber')
