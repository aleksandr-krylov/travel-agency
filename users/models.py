from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
ADMIN = 'A'
MANAGER = 'M'
CLIENT = 'C'
STATUS_CHOICES = [
    (ADMIN, 'Администратор'),
    (MANAGER, 'Менеджер'),
    (CLIENT, 'Клиент')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=CLIENT, verbose_name='Статус')

    def __str__(self):
        return f'Профиль - {self.user.username}'

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Профиль' 
        verbose_name_plural = 'Профили'


class ClientProfile(Profile):
    phone_regex = RegexValidator(
        regex=r'^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}',
        message='Телефон введён в неверном формате.'
    )
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    passport = models.CharField(max_length=20, verbose_name='Серия и номер паспорта', null=True, blank=True)
    starts_date = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    expires_date = models.DateField(verbose_name='Действителен до', null=True, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_regex], verbose_name='Номер телефона', null=True, blank=True)


    class Meta:
        db_table = 'ClientProfile'
        verbose_name = 'Профиль клиента' 
        verbose_name_plural = 'Профили клиентов'

