from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
import random

app = Flask(__name__)
class MyForm(FlaskForm):
    name = StringField('name')
    password = PasswordField('pass')
    forever = BooleanField()

@app.route('/')
def render_index():
    '''Main page'''
    return render_template('index.html')


@app.route('/all/')
def render_all():
    '''Page with a list of all tutors'''
    return render_template('all.html')


@app.route('/goals/<goal>/')
def render_goal():
    '''Page of student's goals'''
    return render_template('goal.html')


@app.route('/profiles/<tutor_id>/')
def render_tutor_profile():
    '''Page with info about a certain tutor'''
    return render_template('profile.html')


@app.route('/request/')
def render_request():
    '''Page of selection for a tutor'''
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    '''
    Route for an application of seeking a tutor is successful sending
    '''
    return render_template('request_done.html')


@app.route('/booking/<tutor_id>/<week_day>/<time>/')
def render_booking():
    '''Booking page'''
    return       

@app.route('/booking_done/')
def render_booking_done():
    '''Route. Application for a tutor is successful sending'''
    return


#entry point
if __name__ == '__main__':
 
    app.run(debug=True)
    #app.run()