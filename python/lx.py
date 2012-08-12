# coding: utf-8

import urllib
import lxml.html
# подключили библиотеку lxml

page = urllib.urlopen("http://habrahabr.ru/")
# Открываем наш любимый Хабр

doc = lxml.html.document_fromstring(page.read())
# Получили HTML-код главной страницы Хабра

for topic in doc.cssselect('h2.entry-title a.topic'):
    print topic.text
        # выводим на экран названия топиков.
