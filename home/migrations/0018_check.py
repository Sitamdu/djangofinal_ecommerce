# Generated by Django 4.1.5 on 2023-01-20 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('slug', models.TextField()),
                ('checkout', models.BooleanField(default=True)),
                ('final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cart')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
