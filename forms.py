from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, RadioField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Email

from func import get_data_from_db


class BookingForm(FlaskForm):
    '''Booking form for a class with a tutor'''
    name = StringField('Вас зовут', [InputRequired('Пожалуйста, введите ваше имя')])
    phone = StringField('Ваш телефон', [InputRequired('Пожалуйста, введите ваш номер телефона')])
    submit = SubmitField('Записаться на пробный урок')



class RequestForm(FlaskForm):
    '''Request form for a tutor search'''
    goal = RadioField(
        'Какая цель занятий?', 
        choices = [(key, ' '.join(value)) for key, value in get_data_from_db(option='goals').items()], default='travel')

    time_for_practice = RadioField(
        'Сколько времени есть?', 
        choices = [(key, value) for key, value in get_data_from_db(option='time_for_practice').items()], default='limit1_2')

    name = StringField('Вас зовут', [InputRequired('Пожалуйста, введите ваше имя')])
    phone = StringField('Ваш телефон', [InputRequired('Пожалуйста, введите ваш номер телефона')])
    submit = SubmitField('Найдите мне преподавателя!')