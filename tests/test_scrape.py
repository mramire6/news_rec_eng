from nlp_model.scrape import Scrape
import pytest

###### Dummy test data for test_scrape.py #######

dummy_working_url = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c-4d5d-b4b7-891113b56233.html"
dummy_not_working_url = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c.html"
dummy_working_incorrect_url = "https://www.axios.com/politics-policy/election"

#####################

@pytest.fixture(scope='module')
def scrape_correct_url():
    s = Scrape(dummy_working_url)
    s.get_request_object()
    s.check_status_code()
    s.get_web_page()
    s.soupify_webpage()
    s.isolate_article()
    s.isolate_text()
    s.isolate_headline()
    s.isolate_authors()
    s.isolate_section()
    s.find_word_count()
    return s

@pytest.fixture(scope='module')
def scrape_404_url():
    s = Scrape(dummy_not_working_url)
    s.get_request_object()
    return s

@pytest.fixture(scope='module')
def scrape_incorrect_working_url():
    s = Scrape(dummy_working_incorrect_url)
    s.get_request_object()
    s.check_status_code()
    s.get_web_page()
    s.soupify_webpage()
    return s

#######################

# Test whether request object was made correctly
def test_constructor1(scrape_correct_url):
    assert scrape_correct_url.soup_ing['ro'] is not None

def test_constructor2(scrape_404_url):
    assert scrape_404_url.soup_ing['ro'] is not None

def test_constructor3(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.soup_ing['ro'] is not None

# Test whether status code was correctly identified or exception raised
def test_web_page_found1(scrape_correct_url):
    assert scrape_correct_url.soup_ing['code'] == 200

def test_web_page_found1(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.soup_ing['code'] == 200

def test_web_page_found1(scrape_404_url):
    with pytest.raises(Exception):
        assert scrape_404_url.check_status_code()

# Test whether a soup was made
def test_soupify_webpage1(scrape_correct_url):
    assert scrape_correct_url.soup_ing['soup'] is not None

def test_soupify_webpage2(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.soup_ing['soup'] is not None

# Test whether an article was found or not
def test_isolate_article1(scrape_correct_url):
    assert scrape_correct_url.main_info['article'] is not None

def test_isolate_article2(scrape_incorrect_working_url):
    with pytest.raises(Exception):
        assert scrape_incorrect_working_url.isolate_article()

# Test whether data was able to be extracted from article
def test_isolate_text(scrape_correct_url):
    assert scrape_correct_url.main_info['main_text'] is not None

def test_isolate_main_headline(scrape_correct_url):
    assert scrape_correct_url.main_info['headline'] is not None
    assert isinstance(scrape_correct_url.main_info['headline'], str)

def test_isolate_main_authors(scrape_correct_url):
    assert len(scrape_correct_url.main_info['authors']) >= 1
    assert isinstance(scrape_correct_url.main_info['authors'][0], str)

def test_isolate_section(scrape_correct_url):
    assert scrape_correct_url.main_info['section'] is not None
    assert isinstance(scrape_correct_url.main_info['section'], str)

def test_find_word_count(scrape_correct_url):
    assert scrape_correct_url.main_info['word_count'] is not None
    assert scrape_correct_url.main_info['word_count'] > 0
    assert isinstance(scrape_correct_url.main_info['word_count'], int)
