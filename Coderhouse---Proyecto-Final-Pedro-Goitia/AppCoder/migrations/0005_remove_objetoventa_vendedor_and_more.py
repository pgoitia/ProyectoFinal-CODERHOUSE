# Generated by Django 4.1 on 2023-02-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_rename_nombre_objetoventa_objeto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objetoventa',
            name='vendedor',
        ),
        migrations.AlterField(
            model_name='objetoventa',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
