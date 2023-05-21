# Generated by Django 4.2.1 on 2023-05-21 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100, null=True)),
                ('cpf', models.CharField(max_length=14, null=True)),
                ('logradouro', models.CharField(max_length=255, null=True)),
                ('nro', models.IntegerField(null=True)),
                ('telefone', models.CharField(max_length=16, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
