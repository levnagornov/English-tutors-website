from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def render_index():
    ''' Main page '''
    return render_template('index.html')


@app.route('/all/')
def render_all():
    ''' Page with a list of all teachers '''
    return render_template('all.html')


@app.route('/goals/<goal>/')
def render_goal():
    ''' Page of student's goals '''
    return render_template('goal.html')


@app.route('/profiles/<teacher_id>/')
def render_teacher_profile():
    ''' Page with info about a certain teacher '''
    return render_template('profile.html')


@app.route('/request/')
def render_request():
    ''' Page of selection for a teacher '''
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    ''' Route for an application of seeking a teacher is successful sending '''
    return render_template('request_done.html')


@app.route('/booking/<teacher_id>/<week_day>/<time>/')
def render_booking():
    ''' Booking page '''
    return       

@app.route('/booking_done/')
def render_booking_done():
    ''' Route. Application for a teacher is successful sending '''
    return


#entry point
if __name__ == '__main__':
 
    app.run(debug=True)
    #app.run()