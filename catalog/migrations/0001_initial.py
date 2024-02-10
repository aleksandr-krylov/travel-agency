# Generated by Django 2.2.2 on 2019-12-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(default='default_category.jpg', upload_to='tour_pics', verbose_name='Путь к картинке')),
            ],
            options={
                'verbose_name': 'категория тура',
                'verbose_name_plural': 'категории туров',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
                'db_table': 'Country',
            },
        ),
    ]
