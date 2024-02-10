# Generated by Django 2.2.2 on 2019-12-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog-default-image.png', upload_to='blog_pics', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique_for_date='date_posted', verbose_name='Заголовок'),
        ),
    ]