# Generated by Django 4.1.5 on 2023-01-19 06:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
