# Generated by Django 3.1.4 on 2021-02-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20210215_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('pais', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
