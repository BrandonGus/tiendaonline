# Generated by Django 5.1.1 on 2024-10-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0002_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La direccion'),
        ),
    ]
