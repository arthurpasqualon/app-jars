from django import forms
from django.contrib.auth import password_validation
from material import Layout, Row

from django.contrib.auth.forms import PasswordResetForm

from apps.accounts.models import User # ADD


def clean_email(email, user=None, company=None):
    email = email.strip().lower()
    email_exists = User.objects.filter(email=email)
    if user:
        email_exists = email_exists.exclude(id=user.id)
    if email_exists.exists():
        raise forms.ValidationError("O email informado já está sendo utilizado por outra conta.")
    return email


class UserAdminForm(forms.ModelForm):
    send_invite = forms.BooleanField(required=False, label="(Re)Enviar Convite")
    password_reset = forms.CharField(label="Redefinir senha:", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'email_confirmed',
                  'is_active', 'is_volunteer', 'is_superuser',
                  'profile_picture', 'institution', 'is_principal', 'password_reset']

    def save(self, commit=True):
        user = super().save(commit)
        password_new = self.cleaned_data.get('password_reset')
        if password_new:
            user.set_password(password_new)
            user.save(update_fields=['password'])
        return user


class MyAccountForm(forms.ModelForm):
    password_new = forms.CharField(required=False, label="Nova senha", widget=forms.PasswordInput,
                                   help_text="Opcional, deixe em branco para não alterar sua senha.")
    password_check = forms.CharField(label="Informe sua senha atual", widget=forms.PasswordInput,
                                     help_text=("Por motivos de segurança, solicitamos a confirmação "
                                                "da sua senha atual para permitir alterações nas "
                                                "informações acima."))

    layout = Layout(
        Row('first_name', 'last_name'),
        Row('email'),
        Row('password_new'),
        Row('password_check')
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password_new']

    def clean_email(self):
        return clean_email(self.cleaned_data.get('email'), self.instance, self.instance.company)

    def clean_password_new(self):
        password_new = self.cleaned_data.get('password_new')
        if password_new:
            password_validation.validate_password(password=password_new)
        return password_new

    def clean_password_check(self):
        password_check = self.cleaned_data.get('password_check')
        if not self.instance.check_password(password_check):
            raise forms.ValidationError("A senha atual está incorreta.", code='invalid')
        return password_check

    def save(self, commit=True):
        user = super().save(commit=commit)
        password_new = self.cleaned_data.get('password_new')
        if password_new:
            user.set_password(password_new)
            user.save(update_fields=['password'])
        return user


class MyAccountProfilePictureForm(forms.ModelForm):
    use_profile_picture = forms.BooleanField(required=False, label="Usar minha foto")
    profile_image = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['use_profile_picture', 'profile_image', 'profile_picture']

    def clean_use_profile_picture(self):
        use_profile_picture = self.cleaned_data.get('use_profile_picture')
        if use_profile_picture and \
                not self.files.get('profile_picture') and \
                not self.instance.profile_picture:
            raise forms.ValidationError("Envie um arquivo.")
        return use_profile_picture
