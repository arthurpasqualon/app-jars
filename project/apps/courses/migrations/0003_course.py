# Generated by Django 2.0.7 on 2018-12-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('slug', models.SlugField(blank=True, verbose_name='slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/img', verbose_name='image')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('from_date', models.DateTimeField(blank=True, null=True, verbose_name='data de início')),
                ('to_date', models.DateTimeField(blank=True, null=True, verbose_name='data final')),
                ('institution', models.CharField(blank=True, max_length=100, null=True, verbose_name='instituicao de ensino')),
                ('program', models.CharField(blank=True, max_length=100, null=True, verbose_name='programa')),
                ('classmate', models.CharField(blank=True, max_length=100, null=True, verbose_name='aluno')),
                ('frequency', models.CharField(blank=True, max_length=100, null=True, verbose_name='frequencia')),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'ordering': ['from_date'],
            },
        ),
    ]
