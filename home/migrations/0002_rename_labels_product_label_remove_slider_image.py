# Generated by Django 4.1.5 on 2023-01-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='labels',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
    ]
