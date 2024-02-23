from django import forms
from django.contrib.auth.forms import UserCreationForm
from social_book_app.models import CustomUser
from .models import UploadedFile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=255, required=True)
    birth_year = forms.IntegerField(required=True)
    public_visibility = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'birth_year', 'public_visibility', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        user.birth_year = self.cleaned_data['birth_year']
        user.public_visibility = self.cleaned_data['public_visibility']

        if commit:
            user.save()

        return user


class UploadedFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UploadedFileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'file', 'visibility', 'cost', 'year_published']

    def save(self, commit=True):
        uploaded_file = super().save(commit=False)
        uploaded_file.user = self.user
        if commit:
            uploaded_file.save()
        return uploaded_file