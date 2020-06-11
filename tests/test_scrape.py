from nlp_model.scrape import Scrape
import pytest

@pytest.fixture
def scrape():
    url = ("https://www.axios.com/facebook-employees-stage-virtual-walkout-"
    "7f28483e-d59c-4d5d-b4b7-891113b56233.html")
    return Scrape(url)

def test_constructor(scrape):
    assert isinstance(scrape, Scrape)
    scrape.get_webpage()
    scrape.check_status_code()
    assert scrape.status_code == 200

def test_soupify(scrape):
    parser_type = 'html.parser'
    scrape.soupify_webpage(parser_type)
    assert scrape.soup is not None

# def test_isolate_main_article(scrape):
#     scrape.isolate_main_article()
#     assert scrape.main_article is not None

# def test_isolate_main_article(scrape):
#     scrape.isolate_main_article()
#     assert isinstance(scrape.main_text, String)

# def test_isolate_main_headline(scrape):
#     scrape.isolate_main_headline()
#     assert isinstance(scrape.main_headline, String)

# def test_isolate_main_authors(scrape):
#     scrape.isolate_main_authors()
#     assert isinstance(scrape.main_authors,List)

# def test_isolate_main_tags(scrape):
#     scrape.isolate_main_tags()
#     assert isinstance(scrape.main_tags,String)

# def test_word_count(scrape):
#     scrape.word_count()
#     assert scrape.word_count is not None
#     assert scrape.word_count > 0
