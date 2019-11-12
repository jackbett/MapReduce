import warc
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from langdetect import detect
import csv
from warcio.archiveiterator import ArchiveIterator

def html_to_text (body):
    soup = BeautifulSoup(body.decode('utf-8','ignore'), 'html.parser')
    texts = soup.findAll(text=True)
    actual_text = filter(removing_tags, texts)  
    return u" ".join(t.strip() for t in actual_text)


def removing_tags (element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def request_URLS (URLs, articles):
    subtopic = ["sports", "basketball", "cricket", "tennis", "soccer", "football"]
    for x in range(15000, 20000):
        if any(topic in URLs[x] for topic in subtopic):
            try:
                html = urllib.request.urlopen(URLs[x]).read()
                text = html_to_text(html)
                lang = detect(text)
                if lang == 'en' and len(articles) != 500: 
                    articles.append(text)
                    print(URLs[x])
            except:
                continue

    
    # print(articles[4].encode("utf-8"))

def write_to_csv (given_articles) : 
    with open('ccarticles.csv', mode = 'a', newline='\n', encoding = 'utf-8-sig') as articles:
        articleWriter = csv.writer(articles, delimiter = ',')
        for i in given_articles: 
            articleWriter.writerow([i])
    articles.close()



articles = [] 
URLs = []

with warc.open("WET Files/CC-MAIN-20180715183800-20180715203800-00007.warc.wet") as f:
    for record in f:
        if record.url != None: 
            URLs.append(record.url)


request_URLS(URLs, articles)
write_to_csv(articles)


