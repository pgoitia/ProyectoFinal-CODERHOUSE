# Generated by Django 4.1 on 2023-02-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_objetoventa_delete_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetoventa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
