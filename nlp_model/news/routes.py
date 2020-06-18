from flask import Blueprint, render_template, url_for, redirect
from nlp_model.news.forms import SectionDateNewsForm, LatestNewsForm

news_bp = Blueprint('news_bp', __name__, template_folder='templates')

@news_bp.route('/news', methods=['GET', 'POST'])
def news():
    """ Ask the user to select what kind of news they want """
    section_date_form = SectionDateNewsForm()
    latest_form = LatestNewsForm()
    if section_date_form.submit.data:
        return redirect(url_for('news_bp.news_latest'))
    return render_template('news/news_home.html', section_date_form=section_date_form)

@news_bp.route('/news/latest')
def news_latest():
    return render_template('news/news_latest.html')

    # if form.validate():
    #     section = form.section.data
    #     date = form.section.data
    #     if section:
    #         if date:
    #             date = date.replace('-','/')
    #             return redirect('/news/<section>/<date>')
    #         return redirect('/news/<section>')

# @news_bp.route('/news/latest', methods=['GET', 'POST'])
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

# @news_bp.route('/news/<string:section>')
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

# @news_bp.route('/news/<string:section>/<string:date>')
# def news_section_date(section, date):
#     """
#     Display headlines from top 10 most recent news articles
#     for that section and that day
#     """
#     pass
