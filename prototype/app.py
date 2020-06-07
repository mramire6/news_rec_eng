from flask import Flask

app = Flask(__name__)

##################
@app.route('/')
def homepage():
    """
    Home page of the application. Will explain purpose and display results.
    """
    pass

@app.route('/about')
def aboutme():
    """
    About me page that links to my professional website / github / Linkedin
    """
    pass

@app.route('/results')
def results():
    """
    This URI will allow the user to select a section (e.g. technology)
    and a topic (e.g. robotics) and the most recent article will pop up.
    Next to it will be my suggested next article to read based on NLP models
    Next to it will also be the Go Deeper article tha Axios recommends
    for comparison purposes
    """
    pass

@app.route('/axiosanalytics')
def axiosanalytics():
    """
    This URI will detail analytics from the web scraping
    For example, how many authors published articles today?
    Which sections had the most articles?
    AVerage word count for the day?
    """
    pass

@app.route('/modelanalytics')
def modelanalytics():
    """
    This URI will detail logging information on the web scraping and NLP model
    For example it might say when was the most recent update made to the database,
    it might show what the trending words were for each section and how the frequency of these words
    changed over time
    Another example is it might have version and logging information on how the model deployment is doing

    The idea is to open the hood to some of the backend processes that are happening like if the build failed, etc.
    """
    pass
