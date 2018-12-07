import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# from project.core.helpers import UploadsPath
from .managers import AccountsSettingsManager, UserManager


class AccountsSettings(models.Model):
    objects = AccountsSettingsManager()

    class Meta:
        verbose_name = "configurações das contas"
        verbose_name_plural = "configurações das contas"

    def __str__(self):
        return "Configurações das contas"


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    first_name = models.CharField(max_length=64, verbose_name="primeiro nome")
    
    last_name = models.CharField(max_length=64, verbose_name="último nome")
    full_name = models.CharField(max_length=128, blank=True, verbose_name="nome completo")
    email = models.EmailField(unique=True, max_length=96, verbose_name="email")
    email_confirmed = models.DateTimeField(blank=True, null=True, verbose_name="email confirmado")
    is_active = models.BooleanField(default=True, verbose_name="ativo")
    is_volunteer = models.BooleanField(default=False, verbose_name="voluntario")
    profile_image = models.SmallIntegerField(default=1, verbose_name="imagem do perfil")
    profile_picture = models.ImageField(upload_to='accounts/img', null=True, blank=True, verbose_name='image')
    # institution = models.ForeignKey('Institution', blank=True, null=True, on_delete=models.PROTECT,
                                # verbose_name="instituição")
    institution = models.CharField(max_length=128, blank=True, verbose_name="nome instituicao")
    is_principal = models.BooleanField(default=False, verbose_name="diretor da escola")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="UUID")
    is_staff = models.BooleanField(('staff status'),default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    __original_email = None

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.__original_email = self.email

    def __str__(self):
        return self.get_full_name()

    def profile_image_url(self):
        if self.profile_image == 0 and self.profile_picture:
            return self.profile_picture.url
        return static('apps_accounts/img/profile-image-{}.png'.format(self.profile_image))

    def get_full_name(self):
        return self.full_name
        get_full_name.short_description = "nome completo"

    def get_short_name(self):
        return self.first_name
        get_short_name.short_description = "primeiro nome"

    def save(self, *args, **kwargs):
        self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
        instance = super().save(*args, **kwargs)
        self.__original_email = self.email
        return instance
    
    def delete(self, *args, **kwargs):
        self.img.delete()
        super(User, self).delete(*args, **kwargs)

#  TODO extender de um usuario para poder rolar o delete user 

# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile')
#     age = models.IntegerField()
#     gender = models.BooleanField()

# TODO 

#  checa o curso_id ou evento_id e confere se a frequencia é True

#     def participants(self):
#         if self.course is not None:
#             return User.objects.participants(self)
#         return None
    
#     def event_participations(self):
#             return User.objects.event_participations(self)
#         return None

#     def can_emmit_certification(self, id=None):
#         if id:
#             return self.classes().filter(id=id).exists()
#             return self.event_participations().filter(id=id).exists()
#         return False


#  Class Institution()