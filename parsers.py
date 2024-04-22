from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="caption")
        for item in news:
            title = item.find("h3").text
            href = item.find('a').get('href')
            author = item.find("a", class_="topic-info-author-link").text.strip()
            print(author)

    def run(self):
        self.get_html()
        self.parsing()
