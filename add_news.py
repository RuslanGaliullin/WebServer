from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNewsForm(FlaskForm):
    name = StringField('Название книги', validators=[DataRequired()])
    content = TextAreaField('Ваше мнение', validators=[DataRequired()])
    link = TextAreaField('Ссылка на краткое содержание')
    submit = SubmitField('Добавить')
