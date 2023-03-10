# Generated by Django 4.1.5 on 2023-01-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
                ('comment', models.TextField()),
                ('star', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]
