from flask import Blueprint, url_for, render_template

nlp_pred_model_analytics_bp = Blueprint('nlp_pred_model_analytics_bp', __name__)

@nlp_pred_model_analytics_bp.route('/scrape_analytics')
def scrape_analytics():
    """
    This URI will detail analytics from the web scraping
    For example, how many authors published articles today?
    Which sections had the most articles?
    AVerage word count for the day?
    """
    return render_template(url_for('nlp_pred_model_analytics_bp.scrape_analytics',
                                   title='Web Scrape Analytics'))
