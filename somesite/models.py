from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель для авторизации пользователя"""
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    patronymic = models.CharField(verbose_name='отчество', max_length=250,
                                  null=False, blank=True, default='',
                                  help_text='отчество',)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='время обновления')

    def get_fio(self):
        """ Получение ФИО в формате Иванов И.И."""
        last_name = self.last_name
        first_name = self.first_name[:1] + "." if self.first_name else ""
        patronymic = self.patronymic[:1] + "." if self.patronymic else ""
        return f"{last_name} {first_name}{patronymic}"

    def __str__(self):
        """
        :return: переопределение представление
        """
        if self.first_name or self.patronymic or self.last_name:
            return f'{self.first_name if self.first_name else ""} ' \
                   f'{self.patronymic if self.patronymic else ""} ' \
                   f'{self.last_name if self.last_name else ""} '
        else:
            return 'Пользователь'


class Orderer(models.Model):
    """Модель заказчика"""

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                help_text='пользователь')


class Contractor(models.Model):
    """Модель исполнителя"""
    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                help_text='пользователь')
    slug = models.SlugField(max_length=255,
                            db_index=True,
                            default='slug',
                            verbose_name="slug",
                            help_text='slug')
    experience = models.TextField(verbose_name='о себе',
                                  blank=True,
                                  default='')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='время обновления')


