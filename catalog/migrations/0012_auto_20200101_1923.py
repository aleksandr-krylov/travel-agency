# Generated by Django 2.2.2 on 2020-01-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20200101_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]