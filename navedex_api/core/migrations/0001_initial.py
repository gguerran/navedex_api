# Generated by Django 3.1 on 2020-08-15 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Naver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('birthdate', models.DateField(verbose_name='Data de nascimento')),
                ('job_role', models.CharField(max_length=50, verbose_name='Cargo')),
                ('admission_date', models.DateField(verbose_name='Data de admissão')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
            ],
            options={
                'verbose_name': 'naver',
                'verbose_name_plural': 'navers',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('navers', models.ManyToManyField(blank=True, related_name='projects', to='core.Naver', verbose_name='Navers')),
            ],
            options={
                'verbose_name': 'projeto',
                'verbose_name_plural': 'projetos',
                'ordering': ('name',),
            },
        ),
    ]
