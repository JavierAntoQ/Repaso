# Generated by Django 3.1.4 on 2021-02-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=110),
        ),
        migrations.AlterField(
            model_name='reseña',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]