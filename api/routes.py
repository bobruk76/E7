from api import app
from flask import Flask, request, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-message', methods=['GET'])
def new_message_get():
    return render_template('newmessage.html')

# @app.route('/new-message', action =['post',])
# def new_message_post():
#     message = request.form.get('message')
#     return render_template('mewmessage.html')