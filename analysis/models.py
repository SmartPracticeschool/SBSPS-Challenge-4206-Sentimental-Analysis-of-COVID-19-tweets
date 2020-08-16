from django.db import models
from django.contrib.auth.models import User
import datetime

class Analysis(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  date_created = models.DateTimeField(default=datetime.datetime.now())
  create_by = models.ForeignKey(User, on_delete=models.CASCADE)
  statewise_tweets = models.TextField(null=True, blank=True)
  datewise_tweets = models.TextField(null=True, blank=True)
  trending_tweets = models.TextField(null=True, blank=True)
  trending_keywords = models.TextField(null=True, blank=True)

  class Meta:
    verbose_name_plural = "Analysis"

  def __str__(self):
    return f'{self.title} - {self.create_by}'


class Keyword(models.Model):
  keyword = models.CharField(max_length=50)
  analysis = models.ForeignKey(Analysis, related_name='keywords', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.keyword} - {self.analysis}'

class DefaultKeyword(models.Model):
  keyword = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.keyword}'