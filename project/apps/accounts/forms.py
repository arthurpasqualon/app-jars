from django import forms
from django.contrib.auth import password_validation
from material import Layout, Row

from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student

# class UserForm(UserChangeForm):
#     class Meta:
#         model = User

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     student_kwargs = kwargs.copy()
    #     if kwargs.has_key('instance'):
    #         self.student = kwargs['instance'].student
    #         student_kwargs['instance'] = self.student
    #     self.student_form = StudentForm(*args, **student_kwargs)
    #     self.fields.update(self.student_form.fields)
    #     self.initial.update(self.student_form.initial)

    #     # define fields order if needed
    #     self.fields.keyOrder = (
    #         'last_name',
    #         'first_name',
    #         # etc
    #         'address',
    #     )


    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     self.errors.update(self.student_form.errors)
    #     return cleaned_data

    # def save(self, commit=True):
    #     self.student_form.save(commit)
    #     return super(UserForm, self).save(commit)


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


# class MyAccountProfilePictureForm(forms.ModelForm):
#     use_profile_picture = forms.BooleanField(required=False, label="Usar minha foto")
#     profile_image = forms.IntegerField(widget=forms.HiddenInput())

#     class Meta:
#         model = User
#         fields = ['use_profile_picture', 'profile_image', 'profile_picture']

#     def clean_use_profile_picture(self):
#         use_profile_picture = self.cleaned_data.get('use_profile_picture')
#         if use_profile_picture and \
#                 not self.files.get('profile_picture') and \
#                 not self.instance.profile_picture:
#             raise forms.ValidationError("Envie um arquivo.")
#         return use_profile_picture
