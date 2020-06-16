from datetime import date

def find_latest_URLs(soup):
    """ Return list of URLs under the latest stories"""
    latest_stories = soup.find('div',id='maincontent').find('section').find_all('a', class_='title-link')
    return [latest_stories[ind]['href'] for ind in range(len(latest_stories))]

def get_todays_date():
    """ Obtain Today's date in format axios URL uses"""
    return str(date.today().year) + '/' + str(date.today().month) + '/' + str(date.today().day)

def get_url_for_section(section):
    return 'https//www.axios.com/' + section

def get_url_for_section_and_date(section, date):
    return 'https://www.axios.com/' + section + '/' + date

def find_URLs_by_section_or_date(soup):
    """ Return list of URLs for a specific section or section and date """
    all_urls = soup.find_all('a', class_='gtm-content-click title-link')
    return [all_urls[url_num]['href'] for url_num in range(len(all_urls))]

