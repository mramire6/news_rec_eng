from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class SectionForm(FlaskForm):
    section = SelectField('Section',
                          choices=['technology', 'politics', 'health'])
    submit = SubmitField('Selected Section')

class TopicForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Selected Topic')

#This is where the forms for the user will live. The user will input what the
#section
