from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    # Define fields
    title = models.CharField(max_length=255,
                             unique_for_date='date_posted',
                             verbose_name='Заголовок')
    description = models.TextField(verbose_name='Краткое содержание')
    image = models.ImageField(default='blog_pics/blog-default-image.png',
                              upload_to='blog_pics',
                              verbose_name='Путь к картинке')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now,
                                       db_index=True,
                                       verbose_name='Дата публикации')
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        """return the unique URL for each blog post"""
        return reverse('blog-post', kwargs={'pk': self.pk})


    def get_remove_from_db_url(self):
        return reverse('blog-post-remove', kwargs={'pk': self.pk})

    def get_number_of_comments(self):
        return self.comment_set.count()

    
    class Meta:
        db_table = 'Post' # table name
        ordering = ['-date_posted']
        # the way how the model is demonstrated on the admin page
        verbose_name = 'статья блога' 
        verbose_name_plural = 'статьи блога'


class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий')
    date_commented = models.DateTimeField(default=timezone.now,
                                          db_index=True, verbose_name='Дата комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')


    def __str__(self):
        return '{} - {}'.format(self.author, self.post.title)


    class Meta:
        db_table = 'Comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии статей блога'
        ordering = ['-date_commented']