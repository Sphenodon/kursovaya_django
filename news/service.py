import time
from multiprocessing import Process
from urllib.request import urlopen

from bs4 import BeautifulSoup as BS

from news.models import NewsFromAssociate


def collect():
    siteUrl = 'https://www.igromania.ru/news/'
    titleSet = set()
    news_linkSet = set()
    img_linkSet = set()
    contentSet = set()
    news_author = 'Игромания'
    while True:
        if info["stop"]:
            break
        text = urlopen(siteUrl).read().decode('utf-8')
        bs = BS(text, 'html.parser')
        blocks = bs.find_all(class_='aubl_item')
        for block in blocks:
            title = block.find('a', class_='aubli_name').getText()
            news_link = 'https://www.igromania.ru' + block.find('a').get('href')
            img_link = block.find('img',).get('src')
            content_text = BS(urlopen(news_link).read().decode('utf-8'), 'lxml')
            content = content_text.find('div', class_='universal_content').getText()

            if not NewsFromAssociate.objects.filter(title=title).exists():
                NewsFromAssociate.objects.create(title=title, content=content, news_link=news_link, news_author=news_author, img_link=img_link)

            titleSet.add(title)
            news_linkSet.add(news_link)
            img_linkSet.add(img_link)
            contentSet.add(content)
        time.sleep(5)


info = {"stop": False}


def start_collect_news_from_igromania():
    info["stop"] = False
    p = Process(name='GenerationNews', target=collect(), )
    p.start()
    p.join()


def stop_collect_news_from_igromania():
    info["stop"] = True
