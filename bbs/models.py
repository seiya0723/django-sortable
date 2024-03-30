from django.db import models

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    sort        = models.IntegerField(verbose_name="並び順")


