import random, os
from flask import Flask, render_template, request
from forms import BookingForm, RequestForm
from func import get_data_from_db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(43)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def render_index():
    '''Main page'''
    all_tutors = get_data_from_db(option='tutors')
    all_goals = get_data_from_db(option='goals')
    random_tutors = random.sample(list(all_tutors), k=6)
    print(all_goals)
    return render_template('index.html', random_tutors=random_tutors, all_goals=all_goals)


@app.route('/all/')
def render_all():
    '''Page with a list of all tutors'''
    all_tutors = get_data_from_db(option='tutors')
    return render_template('all.html', all_tutors=all_tutors)


@app.route('/goals/<goal>/')
def render_goal(goal):
    '''Page of student's goals'''
    all_tutors = get_data_from_db(option='tutors')
    all_goals = get_data_from_db(option='goals')
    tutors_by_goal = [
        tutor for tutor in all_tutors if goal in tutor['goals']
        ]   
    return render_template('goal.html', goal=goal, tutors_by_goal=tutors_by_goal, all_goals=all_goals)


@app.route('/profiles/<int:tutor_id>/')
def render_tutor_profile(tutor_id):
    '''Page with info about a certain tutor'''
    all_tutors = get_data_from_db(option='tutors')
    days_of_week = get_data_from_db(option='days_of_week')
    #get dict info by tutor id, catching out of index error
    try:
        tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]
    except IndexError:
        return render_not_found(404)

    return render_template('profile.html', tutor_info=tutor_info, days_of_week=days_of_week)


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


@app.route('/booking/<tutor_id>/<class_day>/<time>/', methods=['GET', 'POST'])
def render_booking(tutor_id, class_day, time):
    '''Booking page'''
    all_days_of_week = get_data_from_db(option='days_of_week')
    all_tutors = get_data_from_db(option='tutors')
    tutor_info = [tutor for tutor in all_tutors if tutor.get('id', 'No match data') == int(tutor_id)][0]
    form = BookingForm()
    if request.method == 'POST':
        client_name, client_phone  = form.name.data, form.phone.data
        return render_template(
            'booking_done.html', 
            all_days_of_week=all_days_of_week,
            form=form, 
            class_day=class_day, 
            time=time, 
            client_name=client_name, 
            client_phone=client_phone)

    return render_template(
        'booking.html', 
        tutor_info=tutor_info, 
        tutor_id=tutor_id, 
        class_day=class_day,
        time=time, 
        all_days_of_week=all_days_of_week,
        form=form)   


#errors handling
@app.errorhandler(500)
def render_server_error(
    error, 
    message='Что-то не так, но мы все починим!'):
    ''' Handling 500 error '''
    return render_template('error.html', message=message), 500


@app.errorhandler(404)
def render_not_found(
    error, 
    message='Ничего не нашлось! Вот неудача, отправляйтесь на главную!'):
    ''' Handling 404 error '''
    return render_template('error.html', message=message), 404


@app.errorhandler(400)
def render_not_found(
    error, 
    message='Бронирование происходит со страницы преподавателя!'):
    ''' Handling 404 error '''
    return render_template('error.html', message=message), 400

#entry point
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()