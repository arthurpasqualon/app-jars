import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# from project.core.helpers import UploadsPath
from .managers import UserManager
from django.contrib.auth.models import AbstractUser

#  TODO extender de um usuario para poder rolar o delete user 

class User(AbstractUser):
    FUNDAMENTAL = 'FD'
    MEDIO = 'MD'
    SUPERIOR = 'SP'
    OUTROS = 'OT'
    MASCULINO = 'M'
    FEMININO = 'F'

    GRADUATION_CHOICES = (
        (FUNDAMENTAL,'Ensino Fundamental'),
        (MEDIO,'Ensino Médio'),
        (SUPERIOR, 'Ensino Superior'),
        (OUTROS,'Outros'),
    )
    GENDER_CHOICES = (
        (FEMININO,'Feminino'),
        (MASCULINO,'Masculino'),
        (OUTROS,'Outros'),
    )

    date_of_birth = models.DateField( null=True, blank=True, verbose_name='data de nascimento' )
    graduation = models.CharField( null=True, blank=True, max_length=10, choices=GRADUATION_CHOICES, default=OUTROS,verbose_name="escolaridade")
    gender = models.CharField( null=True, blank=True, max_length=20, choices=GENDER_CHOICES, default=OUTROS,verbose_name="gênero")
    is_volunteer = models.BooleanField(default=False, verbose_name="voluntario")
    profile_image = models.SmallIntegerField(default=1, verbose_name="imagem do perfil")
    profile_picture = models.ImageField(upload_to='accounts/img', null=True, blank=True, verbose_name='image')
    institution = models.ForeignKey('Institution', blank=True, null=True, on_delete=models.PROTECT,
                                    verbose_name='instituição')
    is_principal = models.BooleanField(default=False, verbose_name="diretor de IE")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="UUID")

    class Meta:
        ordering = ['username']
        verbose_name = 'usuarios'
        verbose_name_plural = 'usuarios'

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


class Institution(models.Model):
    name = models.CharField( max_length=128,verbose_name="nome da IE")
    postal_code = models.CharField( max_length=128,verbose_name="CEP")
    city = models.CharField( max_length=128,verbose_name="cidade")
    street = models.CharField( max_length=128,verbose_name="logradouro")
    number = models.IntegerField(verbose_name="número")
    observation = models.CharField(blank=True, null=True, max_length=128,verbose_name="observacoes")
    email = models.EmailField(null=True, blank=True, verbose_name='email de contato')
    phone = models.CharField(blank=True, null=True, max_length=128,verbose_name="telefone de contato")

    class Meta:
        ordering = ['name']
        verbose_name = 'instituição'
        verbose_name_plural = 'instituições'