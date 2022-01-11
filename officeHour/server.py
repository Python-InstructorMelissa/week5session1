from flask import Flask, render_template, request, redirect, session
import os
from data.user import User
from env import KEY


app = Flask(__name__)
# app.secret_key = os.environ['KEY']
app.secret_key = KEY


@app.route('/')
def index():
    return render_template('index.html', users=User)  # users = what we will call it in html and we set it = to the class name it is associated with

@app.route('/choseUser/', methods=['POST'])
def choseUser():
    session['firstName'] = request.form['firstName']
    return redirect('/viewUser/')

@app.route('/viewUser/')
def viewUser():
    return render_template('viewUser.html', user=User)





if __name__=="__main__":
    app.run(debug=True)