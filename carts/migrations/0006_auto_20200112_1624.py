# Generated by Django 2.2.2 on 2020-01-12 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20200111_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bustourcartitem',
            name='is_ordered',
        ),
        migrations.RemoveField(
            model_name='cruisecartitem',
            name='is_ordered',
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]