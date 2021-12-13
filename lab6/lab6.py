import requests
import re
from bs4 import BeautifulSoup

def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text


url = input(str('Введите ссылку на страницу сайта для роботы с ним: '))


text = get_text(url)
cotext = text.count(' ') + 1

r = requests.get(url)

page = BeautifulSoup(r.text, 'html.parser')
num_tag = len(page.find_all())


html = r.text
soup = BeautifulSoup(html, 'html.parser')
tags = soup.findAll('img')
cotags = len(tags)

aurl = soup.findAll('a')
aurls = len(aurl)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, String, Integer
class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key = True)
    urlsite = Column(String)
    words = Column(Integer)
    tagssite = Column(Integer)
    imgsite = Column(Integer)
    asite = Column(Integer)

from sqlalchemy import create_engine
engine = create_engine("sqlite:///ness.db")
Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
s = session()

news = News(urlsite = url,
            words = cotext,
            tagsite = num_tag,
            imgsite = cotags,
            asite = aurls)

print('Файл создан')
