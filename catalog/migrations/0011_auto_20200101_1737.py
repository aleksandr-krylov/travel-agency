# Generated by Django 2.2.2 on 2020-01-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200101_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='bustour',
            name='services',
            field=models.ManyToManyField(to='catalog.Service', verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='cruise',
            name='services',
            field=models.ManyToManyField(to='catalog.Service', verbose_name='Услуги'),
        ),
    ]