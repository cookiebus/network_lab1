# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, HttpResponse
import urllib
import re, json
from news.models import New

def parse(content):
    start = content.find("<div id=\"endText\" class=\"end-text\">")
    end = content.find("本文来源")   
    content = content[start:end] + "</div></div>"

    while content.find("<iframe") != -1:
        start = content.find("<iframe")
        end = content.find("</iframe>")
        if start == -1 or end == -1:
            break
        content = content[:start] + content[end+9:]

    start = content.find("<div class=\"ep-source cDGray\">")
    end = start + content[start:].find("</div>")
    content = content[:start] + content[end+6:]

    return preview, content


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return '%s' % html.decode('gbk').encode('utf-8')


def getNews(html):
    reg = r'http://news.163.com/\d+.+?\.html'
    newre = re.compile(reg)
    newlist = list(set(re.findall(newre,html)))
    x = 0
    cnt = 0
    for newsurl in newlist:
        html = getHtml(newsurl)
        title = html[html.find('<title>')+7:html.find('</title>')]
        title = title[:title.find("_网易新闻中心")]
        preview, content = parse(html)
        try:
            New.objects.create(title=title, preview=preview, content=content)
        except:
            pass

    return newlist

@staff_member_required
def spider(request):
    html = getHtml("http://news.163.com/")
    newlist = getNews(html)
    return HttpResponse(json.dumps(newlist))
