# Generated by Django 3.1.7 on 2021-03-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[("men's_watches", 'мужские часы'), ('ladies_watches', 'женские часы'), ("couples'_watches", 'парные часы'), ('other', 'разное')], default=('other', 'разное'), max_length=20, verbose_name='Категория'),
        ),
    ]
