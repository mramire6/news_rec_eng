from nlp_model.load_data import *
from nlp_model.scrape import Scrape
from config import Defaults
import pytest

###### Dummy test data for test_load_data.py #######

dummy_axios_main_url = 'https://www.axios.com/'
dummy_axios_section_url = 'https://www.axios.com/technology/'
dummy_axios_section_date_url = 'https://www.axios.com/technology/2020/6/02'

############

def test_find_latest_URLs():
    s = Scrape(dummy_axios_main_url)
    s.get_request_object()
    s.get_web_page()
    s.soupify_webpage()
    result = find_latest_URLs(s.soup_ing['soup'])

    assert len(result) > 0
    for item in result:
        assert isinstance(item,str)

def test_get_todays_date():
    assert get_todays_date() == '2020/6/15'

def test_get_url_for_section():
    for section in Defaults.section_default:
        assert get_url_for_section(section) == 'https//www.axios.com/' + section

def test_get_url_for_section_and_date():
    assert get_url_for_section_and_date('technology', '2020/6/02') == dummy_axios_section_date_url

def test_find_URLs_by_section():
    s = Scrape(dummy_axios_section_url)
    s.get_request_object()
    s.get_web_page()
    s.soupify_webpage()
    result = find_URLs_by_section_or_date(s.soup_ing['soup'])

    assert len(result) > 0
    for item in result:
        assert isinstance(item,str)

def test_find_URLs_by_section_or_date():
    s = Scrape(dummy_axios_section_date_url)
    s.get_request_object()
    s.get_web_page()
    s.soupify_webpage()
    result = find_URLs_by_section_or_date(s.soup_ing['soup'])

    assert len(result) > 0
    for item in result:
        assert isinstance(item,str)
