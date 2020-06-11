import requests
from bs4 import BeautifulSoup

class Scrape():
    def __init__(self,url):
        self.url = url
        self.page = None
        self.status_code = None
        self.soup = None

    def get_webpage(self):
        self.page = requests.get(self.url)

    def check_status_code(self):
        self.status_code = self.page.status_code

    def soupify_webpage(self, parser_type = 'html.parser'):
        self.soup = BeautifulSoup(self.page.content, parser_type)

import requests
from bs4 import BeautifulSoup

URL = ("https://www.axios.com/facebook-employees-stage-virtual-walkout-"
    "7f28483e-d59c-4d5d-b4b7-891113b56233.html")

# ########Functions that work##########
# def get_webpage(URL: str):
#     return requests.get(URL)

# def soupify_webpage(page, parser_type = 'html.parser'):
#     return BeautifulSoup(page.content, parser_type)

# def isolate_main_article(soup):
#     return soup.find('article')

# def isolate_main_text(main_article, class_type = None):
#     if class_type is None:
#         class_type = 'b0w77w-0 jctzOA gtm-story-text p mt-12 mb-20 sm:mt-20'
#     else:
#         class_type = class_type
#     article = soup.find('div', class_=class_type).text
#     return article

# def isolate_main_headline(soup):
#     return soup.title.text

# def isolate_main_authors(main_article):
#     authors_html = main_article.find('div', class_='truncate').find_all('a')
#     authors = [authors_html[ind].text for ind in range(len(authors_html))]
#     return authors

# def isolate_main_tags(main_article):
#     return main_article.find('div').a['href']

# ##################################

# page = get_webpage(URL)
# soup = soupify_webpage(page)

# main_article = isolate_main_article(soup)
# main_tags = isolate_main_tags(main_article)
# main_headline = isolate_main_headline(soup)
# main_authors = isolate_main_authors(main_article)
# main_text = isolate_main_text(main_article)

# print(main_headline)
