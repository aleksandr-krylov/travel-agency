from django.db import models
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
    # Fields
    title = models.CharField(max_length=255,
                             unique_for_date='date_posted',
                             verbose_name='Заголовок')
    image = models.ImageField(default='news_pics/news-default-image.jpg',
                              upload_to='news_pics',
                              verbose_name='Новостная обложка')
    content = models.TextField(verbose_name='Содержание')
    date_posted = models.DateTimeField(default=timezone.now,
                                       db_index=True,
                                       verbose_name='Дата публикации')

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        """return the unique URL for each blog post"""
        return reverse('news-post', kwargs={'pk': self.pk})
   

    class Meta:
        db_table = 'News'
        ordering = ['-date_posted']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
