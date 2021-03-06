# Generated by Django 2.0.7 on 2018-12-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courseparticipation_eventparticipation'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='certificates/img', verbose_name='certificado'),
        ),
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='program/img', verbose_name='imagem'),
        ),
    ]
