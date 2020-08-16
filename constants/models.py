from django.db import models

class NumOfTweetsPerState(models.Model):
  description = models.CharField(max_length=200)
  value = models.IntegerField()

  class Meta:
    verbose_name = "Number of tweets per state"
    verbose_name_plural = "Number of tweets per state"

    def __str__(self):
      return f'{self.description}'


class NumOfTweetsPerDay(models.Model):
  description = models.CharField(max_length=200)
  value = models.IntegerField()

  class Meta:
    verbose_name = "Number of tweets per day"
    verbose_name_plural = "Number of tweets per day"

    def __str__(self):
      return f'{self.description}'


class DaysOfTrendingTweets(models.Model):
  description = models.CharField(max_length=200)
  value = models.IntegerField()

  class Meta:
    verbose_name = "Days of trending tweets"
    verbose_name_plural = "Days of trending tweets"

    def __str__(self):
      return f'{self.description}'


class NoOfPopularTweets(models.Model):
  description = models.CharField(max_length=200)
  value = models.IntegerField()

  class Meta:
    verbose_name = "Number of popular tweets"
    verbose_name_plural = "Number of popular tweets"

  def __str__(self):
    return f'{self.description}'


class NoOfTrendingKeywords(models.Model):
  description = models.CharField(max_length=200)
  value = models.IntegerField()

  class Meta:
    verbose_name = "Number of Trending Keywords"
    verbose_name_plural = "Number of Trending Keywords"

  def __str__(self):
    return f'{self.description}'