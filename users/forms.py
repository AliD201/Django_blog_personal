from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# registration form 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # save to the user model ( dB)
        model = User
        # what form fields to use and in what order
        fields =[
            'username',
            'email',
            'password1',
            'password2',
        ]


#  update user profile 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # save to the user model ( dB)
        model = User
        # what form fields to use and in what order
        fields =[
            'username',
            'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    # image = forms.ImageField(default ='default.jpg', upload_to='profile_pics', attr={'class':'formfix'})
    class Meta:
        # save to the user model ( dB)
        model = Profile
        # what form fields to use and in what order
        fields =[
            'image',
        ]