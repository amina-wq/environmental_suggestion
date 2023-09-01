from django.db import models
from django.utils import timezone


class Suggestions(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'suggestion'
        ordering = ('-date_time', 'title')
        verbose_name = 'Creating suggestion'
        verbose_name_plural = 'Creating suggestions'

    def __str__(self):
        return f'{self.title} {self.description} {self.author} {self.date_time}'
