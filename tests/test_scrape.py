from nlp_model.scrape import Scrape
import pytest

#####################

@pytest.fixture(scope='module')
def scrape_correct_url():
    url = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c-4d5d-b4b7-891113b56233.html"
    s = Scrape(url)
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
    url = "https://www.axios.com/facebook-employees-stage-virtual-walkout-7f28483e-d59c.html"
    s = Scrape(url)
    s.get_request_object()
    return s

@pytest.fixture(scope='module')
def scrape_incorrect_working_url():
    url = "https://www.axios.com/politics-policy/election"
    s = Scrape(url)
    s.get_request_object()
    s.check_status_code()
    s.get_web_page()
    s.soupify_webpage()
    return s

#######################

# Test whether request object was made correctly
def test_constructor1(scrape_correct_url):
    assert scrape_correct_url.ro is not None

def test_constructor2(scrape_404_url):
    assert scrape_404_url.ro is not None

def test_constructor3(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.ro is not None

# Test whether status code was correctly identified or exception raised
def test_web_page_found1(scrape_correct_url):
    assert scrape_correct_url.code == 200

def test_web_page_found1(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.code == 200

def test_web_page_found1(scrape_404_url):
    with pytest.raises(Exception):
        assert scrape_404_url.check_status_code()

# Test whether a soup was made
def test_soupify_webpage1(scrape_correct_url):
    assert scrape_correct_url.soup is not None

def test_soupify_webpage2(scrape_incorrect_working_url):
    assert scrape_incorrect_working_url.soup is not None

# Test whether an article was found or not
def test_isolate_article1(scrape_correct_url):
    assert scrape_correct_url.article is not None

def test_isolate_article2(scrape_incorrect_working_url):
    with pytest.raises(Exception):
        assert scrape_incorrect_working_url.isolate_article()

# Test whether data was able to be extracted from article
def test_isolate_text(scrape_correct_url):
    assert scrape_correct_url.main_text is not None

def test_isolate_main_headline(scrape_correct_url):
    assert scrape_correct_url.title is not None
    assert isinstance(scrape_correct_url.title, str)

def test_isolate_main_authors(scrape_correct_url):
    assert len(scrape_correct_url.authors) >= 1
    assert isinstance(scrape_correct_url.authors[0], str)

def test_isolate_section(scrape_correct_url):
    assert scrape_correct_url.section is not None
    assert isinstance(scrape_correct_url.section, str)

def test_find_word_count(scrape_correct_url):
    assert scrape_correct_url.word_count is not None
    assert scrape_correct_url.word_count > 0
    assert isinstance(scrape_correct_url.word_count, int)




#########################

# @pytest.fixture
# def scrape():
#     url = ("https://www.axios.com/facebook-employees-stage-virtual-walkout-"
#     "7f28483e-d59c-4d5d-b4b7-891113b56233.html")
#     parser_type = 'html.parser'

#     scrape = Scrape(url)
#     scrape.get_request_object()
    # scrape.check_status_code()
    # scrape.get_web_page()
    # scrape.soupify_webpage(parser_type)
    # scrape.isolate_article()
    # scrape.isolate_text()
    # scrape.isolate_headline()
    # scrape.isolate_authors()
    # scrape.isolate_section()
    # scrape.find_word_count()
#     return scrape

# def test_constructor(scrape):
#     assert scrape.ro is not None

# def test_status_code(scrape):
#     assert scrape.code == 200

# def test_get_page(scrape):
#     assert scrape.page is not None

# def test_soupify(scrape):
#     assert scrape.soup is not None

# def test_isolate_article(scrape):
#     assert scrape.article is not None

# def test_isolate_main_article(scrape):
#     assert scrape.main_text is not None

# def test_isolate_main_headline(scrape):
#     assert scrape.title is not None

# def test_isolate_main_authors(scrape):
#     assert len(scrape.authors) >= 1

# def test_isolate_section(scrape):
#     assert scrape.section is not None

# def test_find_word_count(scrape):
#     assert scrape.word_count is not None
#     assert scrape.word_count > 0
