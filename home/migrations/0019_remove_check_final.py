# Generated by Django 4.1.5 on 2023-01-20 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='final',
        ),
    ]
