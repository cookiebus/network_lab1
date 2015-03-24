# -*- coding:iso-8859-1 -*-
from django.shortcuts import render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from news.models import New
import urllib
import re, json
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def next_new(request, id):
    id = int(id)
    while id > 0:
        if New.objects.filter(id=id).exists():
            new = New.objects.get(id=id)
            break
        id -= 1

    if id == 0:
        new = New.objects.all()[0]

    id = new.id - 1

    return render(request, 'index.html', locals())


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

    return content


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return '%s' % html.decode('gbk').encode('utf-8')


def getNews(html):
    reg = r'http://news.163.com/\d+.+?\.html'
    newre = re.compile(reg)
    newlist = re.findall(newre,html)
    x = 0
    cnt = 0
    for newsurl in newlist:
        html = getHtml(newsurl)
        title = html[html.find('<title>')+7:html.find('</title>')]
        title = title[:title.find("_网易新闻中心")]
        New.objects.create(title=title, content=parse(html))

    return newlist

@staff_member_required
def spider(request):
    html = getHtml("http://news.163.com/")
    newlist = getNews(html)
    return HttpResponse(json.dumps(newlist))
