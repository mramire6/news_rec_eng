from flask import render_template, url_for
from nlp_model import app
from nlp_model.forms import SectionForm, TopicForm
from nlp_model.models import Articles, Authors


@app.route('/')
@app.route('/index')
def homepage():
    """
    Home page of the application. Will explain purpose and display results.
    """
    return render_template('index.html', title='Home')

@app.route('/about')
def aboutme():
    """
    About me page that links to my professional website / github / Linkedin
    """
    return render_template('about.html', title='About Me')

@app.route('/nlp_model')
def nlp_model():
    """
    This URI will allow the user to select a section (e.g. technology)
    and a topic (e.g. robotics) and the most recent article will pop up.
    Next to it will be my suggested next article to read based on NLP models
    Next to it will also be the Go Deeper article tha Axios recommends
    for comparison purposes
    """
    return render_template('nlp_model.html', title='NLP Model')

# @app.route('nlp_model/prediction')
# def nlp_model_prediction():
#     """
#     REST API Endpoint for prediction
#     """
#     return render_template('index.html', title='Home')

# @app.route('/nlp_model/model_analytics')
# def nlp_model_analytics():
#     """
#     NLP Model analytics
#     """
#     pass

@app.route('/nlp_model/scrape_analytics')
def scrape_analytics():
    """
    This URI will detail analytics from the web scraping
    For example, how many authors published articles today?
    Which sections had the most articles?
    AVerage word count for the day?
    """
    return render_template('scrape_analytics.html', title='Web Scrape Analytics')


# @app.route('/nlp_model/under_hood')
# def under_hood():
#     """
#     This will display analytics under the hood for the design
#     CD/CI used, TDD design, number of builds, number of tests, etc.
#     Number of features. Logging / versioning / information
#     """
#     pass
