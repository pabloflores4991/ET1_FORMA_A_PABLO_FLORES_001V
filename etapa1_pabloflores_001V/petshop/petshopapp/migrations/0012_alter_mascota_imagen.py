# Generated by Django 3.2.4 on 2021-06-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0011_alter_mascota_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
