from flask_app import app
from flask import Flask, render_template, redirect, session, request
from ..models import owner

@app.route('/') #GET Same thing as localhost:5000/
def home():
    return render_template('index.html', all_owners = owner.Owner.get_all_owners()) # list of objects

@app.route("/owners/new")
def new_owner():
    
    return render_template("create_owner.html")

# make a route for creating owners