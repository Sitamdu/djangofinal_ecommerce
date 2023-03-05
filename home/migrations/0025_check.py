# Generated by Django 4.1.5 on 2023-01-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField()),
                ('slug', models.TextField()),
                ('checkout', models.BooleanField(default=True)),
            ],
        ),
    ]