from flask import render_template, url_for, redirect
from nlp_model import app
from nlp_model.forms import UserSelectionForm, GetLatestForm
#from nlp_model.save_db import get_latest_URLs

#The top 3 common ways a route will conclude will be with:
#1. generating a page template (i.e. render_template(/...))
#2. providing a response (i.e. jsonify(...) / make_response(..))
#3. redirecting the user somewhere else (i.e. redirect(url_for(/...)))

#You can add variables to routes to make dynamic routes
#This means the route address can change
#/route/<variable_name>/<variable_name>

## GREAT EXAMPLE THAT I COULD ACHIEVE ##

# @app.route('/signup', methods=['GET', 'POST'])
# def signup_page():
#     """User sign-up page."""
#     signup_form = SignupForm(request.form)
#
      # POST: Sign user in
#     if request.method == 'POST':
#         if signup_form.validate():
#
              # Get Form Fields
#             name = request.form.get('name')
#             email = request.form.get('email')
#             password = request.form.get('password')
#             website = request.form.get('website')

              # Query database to see if user exists
#             existing_user = User.query.filter_by(email=email).first()

              # If user does not exist create a new entry in database
#             if existing_user is None:
#                 user = User(name=name,
#                             email=email,
#                             password=generate_password_hash(password, method='sha256'),
#                             website=website)
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user)
#                 return redirect(url_for('main_bp.dashboard'))

              # If user exists flash a message and redirect
#             flash('A user already exists with that email address.')
#             return redirect(url_for('auth_bp.signup_page'))
#     # GET: Serve Sign-up page
#     return render_template('/signup.html',
#                            title='Create an Account | Flask-Login Tutorial.',
#                            form=SignupForm(),
#                            template='signup-page',
#                            body="Sign up for a user account.")

###

@app.route('/')
@app.route('/index')
@app.route('/home')
def homepage():
    """Home page explaining what app does."""
    return render_template('index.html', title='Home')

@app.route('/about')
def aboutme():
    """ About me page
    About me page that links to my professional website / github / Linkedin
    """
    return render_template('about.html', title='About Me')

# @app.route('/news', methods=['GET', 'POST'])
# def news():
#     """ Ask the user to select what kind of news they want """
#     form = UserSelectionForm()
#     if form.latest.data:
#         return redirect(url_for('news_latest'))

#     if form.validate():
#         section = form.section.data
#         date = form.section.data
#         if section:
#             if date:
#                 date = date.replace('-','/')
#                 return redirect('/news/<section>/<date>')
#             return redirect('/news/<section>')

# @app.route('/news/latest', methods=['GET', 'POST'])
# def news_latest():
#     """
#     Display headlines from top 10 most recent news articles overall
#     """
#     form = GetLatestForm()

#     #POST: User wants to load new data
#     if form.latest.data:
#         get_latest_URLs()


#     #GET: Display data
#     else:
#         pass

# @app.route('/news/<string:section>')
# def news_section(section):
#     """
#     Display headlines from top 10 most recent news articles
#     for that section
#     """

#     #Get list of URLs for that particular section
#     list_urls = get_url_for_section(section)

#     #Obtain data for each URL
#     for url in list_urls:
#         s = Scrape(url)
#         s.get_request_object()
#         s.get_web_page()
#         s.soupify_webpage()
#         s.isolate_article
#         text = s.isolate_text()
#         headline = s.isolate_headline()
#         authors = s.isolate_authors()
#         word_count = s.find_word_count()

#     #Add data to database

#     #Retreive Data from Database

# @app.route('/news/<string:section>/<string:date>')
# def news_section_date(section, date):
#     """
#     Display headlines from top 10 most recent news articles
#     for that section and that day
#     """
#     pass

# @app.route('/nlp_model', methods=['GET', 'POST'])
# def nlp_model():
#     """
#     This URI will allow the user to select a section (e.g. technology)
#     and a topic (e.g. robotics) and the most recent article will pop up.
#     Next to it will be my suggested next article to read based on NLP models
#     Next to it will also be the Go Deeper article tha Axios recommends
#     for comparison purposes.
#     """
#     user_section = form.section.data
#     user_topic = form.topic.data
#     user_selection = form.submit.data
#     if user_selection:
#         return render_template('nlp_model.html',
#             title='NLP Model',
#             form=form,
#             user_section=user_section,
#             user_topic=user_topic)
#     return render_template('nlp_model.html',
#             title='NLP Model',
#             form=form)

# @app.route('/nlp_model/load')
# def load_data():
#     """
#     This route will execute
#     """
#     pass

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

# @app.route('/scrape_analytics')
# def scrape_analytics():
#     """
#     This URI will detail analytics from the web scraping
#     For example, how many authors published articles today?
#     Which sections had the most articles?
#     AVerage word count for the day?
#     """
#     return render_template('scrape_analytics.html', title='Web Scrape Analytics')

# @app.route('/nlp_model/under_hood')
# def under_hood():
#     """
#     This will display analytics under the hood for the design
#     CD/CI used, TDD design, number of builds, number of tests, etc.
#     Number of features. Logging / versioning / information
#     """
#     pass
