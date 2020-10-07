from werkzeug.utils import redirect

from api import app
from flask import Flask, request, render_template
from api.forms import MessageForm
from api.service import Message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-message', methods=['GET','POST'])
def new_message_get():
    message_form = MessageForm()
    message_db = Message()
    if request.method == 'POST':
        message = request.form.get('message')
        message_db.set(message)
        return redirect('/')

    return render_template('newmessage.html', form=message_form)

