# Generated by Django 5.1.1 on 2024-10-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
