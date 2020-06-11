from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Length
from config import Defaults


class UserSelectionForm(FlaskForm):
    section = SelectField('Section',
                          choices=Defaults.section_default)
    topic = StringField('Topic', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')

#This is where the forms for the user will live. The user will input what the
#section
