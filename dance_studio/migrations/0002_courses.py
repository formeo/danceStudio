# Generated by Django 5.0.4 on 2024-04-14 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dance_studio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Changed date')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('fk_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dance_studio.company', verbose_name='Company')),
            ],
        ),
    ]
