from nlp_model.scrape import Scrape
from nlp_model.load_data import *
from config import Defaults
from nlp_model.models import Articles, Authors, association

# Case 1: User selects --> News by Section
def get_latest_URLs():
    scrape_latest = Scrape(Defaults.main_url)
    scrape_latest_soup =  scrape_latest.get_soup()
    latest_URLs = find_latest_URLs(scrape_latest_soup['soup'])
    return latest_URLs

def store_latest_URLs_db(latest_URLs):
    #Iterate through each of the URLs
    for url in latest_URLs:
        s = Scrape(url).pipeline()
        for info in s.get_main_info():
            new_article = Articles(section=info['article'],
                                   headline=info['headline'],
                                   main_text=info['main_text'],
                                   date_published=...,
                                   word_count=info['word_count'],
                                   hyper_link=...)
            # new_author = Authors(name=...,
            #                      position=...,
            #                      description=...,
            #                      section=...,
            #                      hyper_link=...)
            db.session.add(new_article)
        db.session.commit()
        print('New Article Added')

# Case 2: User selects --> News by Section and Date

# Case 3: User selects --> News by Latest
