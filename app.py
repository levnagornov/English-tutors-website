import random, os
from flask import Flask, render_template, request, redirect, url_for
from forms import BookingForm, RequestForm
from func import get_data_from_db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(43)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def render_index():
    '''Main page. 
    Contains 6 random tutors, all possible education goals, request for a tutor search form.
    '''

    #getting data from DB for a template
    all_tutors = get_data_from_db(option='tutors')
    all_goals = get_data_from_db(option='goals')

    #generating list of 6 random tutors
    random_tutors = random.sample(list(all_tutors), k=6)

    return render_template('index.html', random_tutors=random_tutors, all_goals=all_goals)


@app.route('/all/')
def render_all():
    '''Page with a list of all tutors and sorting form. 
    Also contains request for a tutor search form.
    '''
    #getting data from DB for a template
    all_tutors = get_data_from_db(option='tutors')

    return render_template('all.html', all_tutors=all_tutors)


@app.route('/goals/<goal>/')
def render_goal(goal):
    '''Page with a list of tutors by certain education goal.'''

    #getting data from DB for a template
    all_tutors = get_data_from_db(option='tutors')
    all_goals = get_data_from_db(option='goals')
    tutors_by_goal = [tutor for tutor in all_tutors if goal in tutor['goals']]

    return render_template('goal.html', goal=goal, tutors_by_goal=tutors_by_goal, all_goals=all_goals)


@app.route('/profiles/<int:tutor_id>/')
def render_tutor_profile(tutor_id):
    '''Page with info about a certain tutor.'''

    #getting data from DB for a template
    all_tutors = get_data_from_db(option='tutors')
    days_of_week = get_data_from_db(option='days_of_week')

    #getting tutor info by tutor_id
    try:
        tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]
    except IndexError:
        return render_not_found(404)

    return render_template('profile.html', tutor_info=tutor_info, days_of_week=days_of_week)


@app.route('/request/', methods=['GET', 'POST'])
def render_request():
    '''Page of selection for a tutor.'''
    form = RequestForm()
    if request.method == 'POST':
        goal = form.goal.data
        time_for_practice = form.time_for_practice.data
        name = form.name.data
        phone = form.phone.data
        if form.validate_on_submit():
            return render_template(
                'request_done.html',
                goal=goal,
                time_for_practice=time_for_practice,
                name=name,
                phone=phone
            )
    return render_template('request.html', form=form)


@app.route('/booking/<tutor_id>/<class_day>/<time>/')
def render_booking(tutor_id, class_day, time):
    '''Booking page.
    This page allows you to book a class with a certain tutor on a chosen day and time. 
    Requires:
    1. tutor_id;
    2. class_day;
    3. time;

    Additional info from db - all_days_of_week and all_tutors.
    '''
    #getting data from DB for a template
    all_days_of_week = get_data_from_db(option='days_of_week')
    all_tutors = get_data_from_db(option='tutors')

    #getting data about certain tutor among all tutors for a temlate
    tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]

    #assign hidden fields of form with passed from URL data
    form = BookingForm()    
    form.class_day.data = class_day
    form.time.data = time
    form.tutor_id.data = tutor_id

    return render_template(
        'booking.html', 
        tutor_info=tutor_info, 
        tutor_id=tutor_id, 
        class_day=class_day,
        time=time, 
        all_days_of_week=all_days_of_week,
        form=form)   


@app.route('/booking_done/', methods=['GET', 'POST'])
def render_booking_done():
    '''This page show only when /booking/ is successfully done.'''

    form = BookingForm()
    if request.method == 'POST' and form.validate_on_submit():

        client_name, client_phone = form.name.data, form.phone.data
        class_day, time = form.class_day.data, form.time.data
        tutor_id = form.tutor_id.data
        all_days_of_week = get_data_from_db(option='days_of_week')
        all_tutors = get_data_from_db(option='tutors')
        tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]
        return render_template(
            'booking_done.html', 
            all_days_of_week=all_days_of_week,
            class_day=class_day, 
            time=time, 
            client_name=client_name, 
            client_phone=client_phone,
            tutor_info=tutor_info,
            tutor_id=tutor_id)

    #Restrict access if /booking/ was ignored
    return render_not_found(404)


#errors handling
@app.errorhandler(500)
def render_server_error(error, msg='Что-то не так, но мы все починим!'):
    '''Handling 500 error.'''
    return render_template('error.html', msg=msg), 500


@app.errorhandler(404)
def render_not_found(
    error, 
    msg='Ничего не нашлось! Вот неудача, отправляйтесь на главную!'):
    ''' Handling 404 error '''

    return render_template('error.html', msg=msg), 404

#entry point
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()