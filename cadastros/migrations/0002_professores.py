# Generated by Django 4.0.1 on 2022-02-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProfessor', models.CharField(max_length=200, verbose_name='Digite seu professor')),
                ('emailProfessor', models.CharField(max_length=200, verbose_name='Digite seu email professor')),
            ],
        ),
    ]
