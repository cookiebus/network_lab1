# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(u'标题', max_length=255)
    content = models.TextField(u'新闻')

    class Meta:
		ordering = ('-id', )
