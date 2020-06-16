from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, DateField
from wtforms.validators import DataRequired, Length
from config import Defaults


class UserSelectionForm(FlaskForm):
    latest = SubmitField('Latest')
    section = SelectField('Section',choices=Defaults.section_default)
    date = DateField('Date', format='%Y-%m-%d')
    #topic = StringField('Topic', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')

class GetLatestForm(FlaskForm):
    latest = SubmitField('Get Latest Articles')

#This is where the forms for the user will live. The user will input what the
#section
