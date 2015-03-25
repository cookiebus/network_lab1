# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(u'标题', max_length=255, unique=True)
    content = models.TextField(u'新闻')
    preview = models.TextField(u'预览')

    class Meta:
		ordering = ('-id', )
