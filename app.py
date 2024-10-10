from flask import Flask, render_template, request, redirect,session
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('useremail')
    password = request.form.get('userpassword')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration Successful. Kindly login to proceed')
    else:
        return render_template('register.html.html', message='Email Already Exista')

    return name + ' ' + email + '' + password

@app.route('/perform_login',  methods=['post'])
def perform_login():

    email = request.form.get('useremail')
    password = request.form.get('userpassword')

    response = dbo.search(email,password)

    if response == 1:
        
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Email/Password')


@app.route('/profile')
def profile():
        return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    search_term = request.form.get('search_term')
    response = api.ner(text, search_term)
    return render_template('ner.html', response= response)


@app.route('/senti')
def senti():
    return render_template('senti.html')

@app.route('/perform_senti', methods=['post'])
def perform_senti():
    text = request.form.get('senti_text')
    response = api.senti(text)
    return render_template('senti.html', response= response)


@app.route('/summery')
def summery():
    return render_template('summery.html')

@app.route('/perform_summery', methods=['post'])
def perform_summery():
    text = request.form.get('summery_text')
    response = api.summery(text)
    return render_template('summery.html', response= response)





app.run(debug=True)