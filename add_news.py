from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class AddNewsForm(FlaskForm):
    name = StringField('Название книги', validators=[DataRequired()])
    content = TextAreaField('Ваше мнение', validators=[DataRequired()])
    link = StringField('Ссылка на краткое содеражание', validators=[DataRequired()])
    foto = StringField('URL на обложку книги', validators=[DataRequired()])
    submit = SubmitField('Добавить')
