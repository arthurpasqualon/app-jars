from django.db import models
from apps.accounts.models import Institution


class CourseManager(models.Manager):

    def search(self, query):
        return self.query_set().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

class EventManager(models.Manager):

    def search(self, query):
        return self.query_set().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

#  MODELS

class Course (models.Model):
    name = models.CharField(max_length=100,verbose_name='nome')
    slug = models.SlugField(blank=True,verbose_name='slug')
    image = models.ImageField(upload_to='courses/img', null=True, blank=True, verbose_name='imagem')
    # future RichTextField
    description = models.TextField (blank=True, verbose_name='descrição')
    from_date = models.DateTimeField(null=True, blank=True, verbose_name='data de início')
    to_date = models.DateTimeField(null=True, blank=True, verbose_name='data final')
    institution = models.ForeignKey(Institution, null=True, blank=True, max_length=100, on_delete=models.CASCADE, verbose_name='instituicao')
    program = models.ForeignKey('Program', null=True, blank=True, max_length=100, on_delete=models.CASCADE, verbose_name='programa')
    frequency = models.CharField(null=True, blank=True, max_length=100,verbose_name='frequencia')
    active = models.BooleanField(default=False,verbose_name='ativo')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='atualizado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="curso"
        verbose_name_plural="cursos"
        ordering = ['from_date']

    objects=CourseManager # Modify the Manager "objects" to activate a custom queryset


class Event (models.Model):
    name = models.CharField(max_length=100,verbose_name='nome')
    slug = models.SlugField(blank=True,verbose_name='slug')
    image = models.ImageField(upload_to='events/img', null=True, blank=True, verbose_name='imagem')
    # future RichTextField
    description = models.TextField (blank=True, verbose_name='descrição')
    from_date = models.DateTimeField(null=True, blank=True, verbose_name='data de início')
    to_date = models.DateTimeField(null=True, blank=True, verbose_name='data final')
    institution = models.ForeignKey(Institution, null=True, blank=True, max_length=100, on_delete=models.CASCADE, verbose_name='instituicao')
    program = models.ForeignKey('Program', null=True, blank=True, max_length=100, on_delete=models.CASCADE, verbose_name='programa')
    frequency = models.CharField(null=True, blank=True, max_length=100,verbose_name='frequencia')
    active = models.BooleanField(default=False,verbose_name='ativo')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='atualizado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="evento"
        verbose_name_plural="eventos"
        ordering = ['from_date']

    objects=EventManager # Modify the Manager "objects" to activate a custom queryset


class Program (models.Model):
    name = models.CharField(max_length=100,verbose_name='nome')
    slug = models.SlugField(blank=True,verbose_name='slug')
    image = models.ImageField(upload_to='events/img', null=True, blank=True, verbose_name='imagem')
    # future RichTextField
    description = models.TextField (blank=True, verbose_name='descrição')
    active = models.BooleanField(default=False,verbose_name='ativo')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='atualizado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="programa"
        verbose_name_plural="programas"
        ordering = ['name']

    
class Module (models.Model):
    program = models.ForeignKey('Program', null=True, blank=True, max_length=100, on_delete=models.CASCADE, verbose_name='programa')
    name = models.CharField(max_length=100,verbose_name='nome')
    slug = models.SlugField(blank=True,verbose_name='slug')
    # future RichTextField
    description = models.TextField (blank=True, verbose_name='descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='atualizado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="aula"
        verbose_name_plural="aulas"
        ordering = ['name']
