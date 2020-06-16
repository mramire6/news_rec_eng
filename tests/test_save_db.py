from nlp_model.save_db import *
import pytest

def test_get_latest_URLS():
    result = get_latest_URLs()
    assert len(result) > 0
    for item in result:
        assert isinstance(item,str)

#Now I am at the point where I need to test if database connections, adding
#data works.
