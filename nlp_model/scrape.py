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

