# Generated by Django 5.1.5 on 2025-02-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_cita'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
