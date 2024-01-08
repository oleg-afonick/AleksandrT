from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    TYPE = (
        ('tank', 'Танк'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    category = models.CharField(max_length=16, choices=TYPE, default='tank', verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    upload = models.ImageField(
        upload_to='uploads/', help_text='Загрузите файл', blank=True, verbose_name='Загрузка файла'
    )

    def __str__(self):
        return f'{self.dateCreation}||{self.title}:{self.text[:20]}'

    def get_absolut_url(self):
        return f'/article/{self.pk}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-dateCreation']


class Comment(models.Model):
    commentPost = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Комментарии')
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Описание')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return f'{self.commentUser} : {self.text} [:20] + ...'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.commentPost_id})

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['id']


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    article = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
