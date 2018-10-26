# Simple Personal Web Chat App using Python

#### For this chat application, we have used *FLASK-SOCKETIO* wrapper of *SOCKET.IO* which is a javascript library used for realtime interaction between server and client machine.

#### Also, we have used *FLASK* web framework which is lightweight framework compare to other frameworks.

#### Demo

![Demo](https://raw.githubusercontent.com/changezkhan/crm/master/chat_app.gif)

## Instructions to install the app ##

* First of all, you'll need to create python virtual environment and activate. Use following lines of code for that.

```
cd <PROJECT_FOLDER>
python -m virtualenv venv
```

* For Unix Users:
```
source venv/bin/activate
```

* For Windows Users:
```
venv/bin/activate
```

* After that, we will install all the required packages using `pip`

```
pip install -r requirements.txt
```

## Instructions to run the application

* After installing all the packages successfully, we wiil run our chat application.

```
python main.py
```

## Instructions to use the application

* Open the URL in your browser window. You'll get to see one login form where you'll have enter desired username to chat with other people.

* Now open, another browser or open the *INCOGNITO* window of the browser and open the same URL.

* Enter different username this time. 

* On right side of window, you'll get to see the list of users which are logged in currently.

* Click on the name of the user to chat with him/her.

* After clicking on the name, you'll get to see one new chat window on same page. And that's it.
