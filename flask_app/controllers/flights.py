from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.flight import Flight


@app.route('/')
def index():
    return render_template('index.html', flights=Flight.getAll())

@app.route('/createFlight/', methods=['POST'])
def createFlight():
    data = {
        'origination': request.form['origination'],
        'destination': request.form['destination'],
        'departTime': request.form['departTime'],
        'arriveTime': request.form['arriveTime'],
        'flightNumber': request.form['flightNumber']
    }
    Flight.save(data)
    return redirect('/')