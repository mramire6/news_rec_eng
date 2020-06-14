import os
import tempfile

import pytest

from nlp_model import nlp_model

@pytest.fixture
def client():
    db_fb, nlp_model.app.config['DATABASE'] = tempfile.mkstemp()
    nlp_model.app.config['TESTING'] = True

    with nlp_model.app.test_client() as client:
        with nlp_model.app.app_context():
            nlp_model.init_db()
        yield client

    os.close(db_fb)
    os.unlink(nlp_model.app.config['DATABASE'])

def test_empty_db(client):
    """
    Start with a blank database.
    """
    rv = client.get('/')
    assert b'No entries here so far' in rv.data
