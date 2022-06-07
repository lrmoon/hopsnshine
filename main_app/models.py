import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField(max_length=50)
    article_text = models.CharField(max_length=200)
    article_date = models.DateTimeField('created At')
    def __str__(self):
        return self.article_title
    def was_created_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)