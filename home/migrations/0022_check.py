# Generated by Django 4.1.5 on 2023-01-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField()),
                ('slug', models.TextField()),
                ('checkout', models.BooleanField(default=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
