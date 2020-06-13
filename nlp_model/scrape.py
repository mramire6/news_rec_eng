import requests
from bs4 import BeautifulSoup

url1 = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c-4d5d-b4b7-891113b56233.html"
url2 = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c.html"
url3 = "https://www.axios.com/politics-policy/election"

class Scrape():
    def __init__(self, url):
        self.url = url
        self.ro = None #checked
        self.page = None #checked
        self.code = None #checked
        self.soup = None #checked
        self.article = None
        self.main_text = None
        self.title = None
        self.authors = None
        self.section = None
        self.word_count = None

    def get_request_object(self):
        self.ro = requests.get(self.url)

    def get_web_page(self):
        self.page = self.ro.content

    def check_status_code(self):
        code = self.ro.status_code
        if code != 200:
            raise Exception('Web page was not found')
        else:
            self.code = code

    def soupify_webpage(self):
        self.soup = BeautifulSoup(self.page, 'html.parser')

    def isolate_article(self):
        temp = self.soup.find('article')
        if temp is None:
            raise Exception('No article was found')
        else:
            self.article = temp

    def isolate_text(self, class_type = None):
        if class_type is None:
            class_type = 'b0w77w-0 jctzOA gtm-story-text p mt-12 mb-20 sm:mt-20'
        else:
            class_type = class_type
        self.main_text = self.article.find('div', class_=class_type).text

    def isolate_headline(self):
        self.title = self.soup.title.text

    def isolate_authors(self):
        authors_html = self.article.find('div', class_='truncate').find_all('a')
        self.authors = [authors_html[ind].text for ind in range(len(authors_html))]

    def isolate_section(self):
        self.section = self.article.find('div').a['href']

    def find_word_count(self):
        self.word_count = len(self.main_text.split())
