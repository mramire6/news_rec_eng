from flask import Blueprint, render_template, url_for

main_bp = Blueprint('main', __name__, template_folder='templates/home')

# #This works
@main_bp.route('/')
@main_bp.route('/index')
def homepage():
    """Home page explaining what app does."""
    return render_template('home.html', title='Home')

@main_bp.route('/about')
def aboutme():
    """ About me page
    About me page that links to my professional website / github / Linkedin
    """
    return render_template('about.html', title='About Me')

