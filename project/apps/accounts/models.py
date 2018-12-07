import uuid

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# from project.core.helpers import UploadsPath
from .managers import UserManager


#  TODO extender de um usuario para poder rolar o delete user 

# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile')
#     age = models.IntegerField()
#     gender = models.BooleanField()
#     is_volunteer = models.BooleanField(default=False, verbose_name="voluntario")
#     profile_image = models.SmallIntegerField(default=1, verbose_name="imagem do perfil")
#     profile_picture = models.ImageField(upload_to='accounts/img', null=True, blank=True, verbose_name='image')
#     # institution = models.ForeignKey('Institution', blank=True, null=True, on_delete=models.PROTECT,
#                                 # verbose_name="instituição")
#     institution = models.CharField(max_length=128, blank=True, verbose_name="nome instituicao")
#     is_principal = models.BooleanField(default=False, verbose_name="diretor da escola")
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="UUID")
#     User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

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