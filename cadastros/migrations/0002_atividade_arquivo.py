# Generated by Django 4.2.1 on 2023-05-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='arquivo',
            field=models.FileField(blank=True, upload_to='pdf/'),
        ),
    ]