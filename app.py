from os import PathLike
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
import random, json


app = Flask(__name__)
class MyForm(FlaskForm):
    name = StringField('name')
    password = PasswordField('pass')
    forever = BooleanField()

def get_data_from_db(option='all'):
    '''Read data from database (json file) and returns a dict of data.
    1. Mode by default is option='all' returns all database.
    2. option: 'tutors' returns data only about tutors.
    3. option: 'goals' returns data only about goals.
    '''
    if option not in ('all', 'tutors', 'goals'):
        raise AttributeError

    with open('db.json', encoding='utf-8') as f:
        db = json.load(f)
        if option == 'all':
            return db
        elif option == 'tutors':
            return db[1]
        elif option == 'goals':
            return db[0]     


@app.route('/')
def render_index():
    '''Main page'''
    return render_template('index.html')


@app.route('/all/')
def render_all():
    '''Page with a list of all tutors'''
    return render_template('all.html')


@app.route('/goals/<goal>/')
def render_goal(goal):
    '''Page of student's goals'''
    return render_template('goal.html')

#DO
@app.route('/profiles/<int:tutor_id>/')
def render_tutor_profile(tutor_id):
    '''Page with info about a certain tutor'''
    all_tutors = get_data_from_db(option='tutors')
    #get dict info by tutor id, catching out of index error
    try:
        tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]
    except IndexError:
        return render_not_found(404)

    return render_template('profile.html', tutor_info=tutor_info)


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
def render_booking(tutor_id, week_day, time):
    '''Booking page'''
    return       

@app.route('/booking_done/')
def render_booking_done():
    '''Route. Application for a tutor is successful sending'''
    return


#errors handling
@app.errorhandler(500)
def render_server_error(
    error, 
    message='Что-то не так, но мы все починим!'
):
    ''' Handling 500 error '''

    return render_template('error.html', message=message), 500


@app.errorhandler(404)
def render_not_found(
    error, 
    message='Ничего не нашлось! Вот неудача, отправляйтесь на главную!'    
):
    ''' Handling 404 error '''

    return render_template('error.html', message=message), 404


#entry point
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()