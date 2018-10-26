""" This script is main file of flask application  """

from flask import session, Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room
from login_form import LoginForm

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'any-random-key-you-can-enter'
SOCKETIO = SocketIO(APP)

@APP.route('/', methods=['GET', 'POST'])
def index():
    """ Redirect to Login Form to enter a chat room """
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET': 
        form.name.data = session.get('name', '')
    return render_template('index.html', form=form)

@APP.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name)

@SOCKETIO.on('my event')
def joined_room(json):
    """ Store user's name and room id in the session dictionary  """
    session['name'] = json['user_name']
    session['room'] = request.sid
    print("JOINED ROOM")
    print(session)
    json['sid'] = request.sid
    join_room(session['room'])
    SOCKETIO.emit('my response', {'json':json, 'room': request.sid}, name=json['user_name'])

@SOCKETIO.on('text')
def send_chat_message(message):
    """ Send chat messages to desired user according the room id  """
    room = session.get('room')
    name = session.get('name')
    msg = message['msg']
    emit('message', {'from': name, 'chat_message': msg, 'room': room}, room=message['room'])

@SOCKETIO.on('left')
def left_chat_room():
    """ When user leaves the room, send left message to all users  """
    SOCKETIO.emit('left room', {'from':session.get('name')}, name=session.get('name'))

if __name__ == '__main__':
    SOCKETIO.run(APP, debug=True)
