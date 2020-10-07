from flask_wtf import FlaskForm
from wtforms import StringField

class MessageForm(FlaskForm):
    message = StringField(u'Сообщение')

class TagCommentForm(FlaskForm):
    tag = StringField(u'Тег')
    comment = StringField(u'Комментарий')