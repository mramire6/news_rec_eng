import requests
from bs4 import BeautifulSoup
import time

class Scrape():
    def __init__(self, url = None, soup = None):
        self.soup_ing = {'url': url,
                         'ro': None,
                         'page': None,
                         'soup': soup}
        self.main_info = {'article': None,
                          'main_text': None,
                          'headline': None,
                          'authors': None,
                          'section': None,
                          'word_count': None}

    def get_request_object(self):
        # As per Axios' editors permission maximum of 10 requests per 60 seconds.
        time.sleep(6)
        self.soup_ing['ro'] = requests.get(self.soup_ing['url'])

    def get_web_page(self):
        self.soup_ing['page'] = self.soup_ing['ro'].content

    def check_status_code(self):
        code = self.soup_ing['ro'].status_code
        if code != 200:
            raise Exception('Web page was not found')
        else:
            self.soup_ing['code'] = code

    def soupify_webpage(self):
        self.soup_ing['soup'] = BeautifulSoup(self.soup_ing['page'], 'html.parser')

    def isolate_article(self):
        temp = self.soup_ing['soup'].find('article')
        if temp is None:
            raise Exception('No article was found')
        else:
            self.main_info['article'] = temp

    def isolate_text(self, class_type = None):
        if class_type is None:
            class_type = 'b0w77w-0 jctzOA gtm-story-text p mt-12 mb-20 sm:mt-20'
        else:
            class_type = class_type
        self.main_info['main_text'] = self.main_info['article'].find('div', class_=class_type).text

    def isolate_headline(self):
        self.main_info['headline'] = self.soup_ing['soup'].title.text

    def isolate_authors(self):
        authors_html = self.main_info['article'].find('div', class_='truncate').find_all('a')
        self.main_info['authors'] = [authors_html[ind].text for ind in range(len(authors_html))]

    def isolate_section(self):
        self.main_info['section'] = self.main_info['article'].find('div').a['href']

    def find_word_count(self):
        self.main_info['word_count'] = len(self.main_info['main_text'].split())

    def get_main_info(self):
        return self.main_info

    ###########

    def get_soup(self):
        self.get_request_object()
        self.check_status_code()
        self.get_web_page()
        self.soupify_webpage()
        return self.soup_ing

    def get_info_articles(self):
        self.isolate_article()
        self.isolate_text()
        self.isolate_headline()
        self.isolate_authors()
        self.section()
        self.find_word_count()
        return self.main_info

    def pipeline(self):
        self.get_request_object()
        self.check_status_code()
        self.get_web_page()
        self.soupify_webpage()
        self.isolate_article()
        self.isolate_text()
        self.isolate_headline()
        self.isolate_authors()
        self.section()
        self.find_word_count()
        return self.main_info




