import json

def get_data_from_db(option='all'):
    '''Read data from database (json file) and returns a dict of data.
    1. Mode by default is option='all' returns dict with all data.
    2. option='tutors' returns dict with only about tutors.
    3. option='goals' returns dict with only about goals.
    4. option='days_of_week' returns dict with days of the week in rus and eng
    5. option='time_for_practice' returns dict with days.
    '''
    if option not in ('all', 'tutors', 'goals', 'days_of_week', 'time_for_practice'):
        raise AttributeError

    with open('db.json', encoding='utf-8') as f:
        db = json.load(f)
        if option == 'all':
            return db
        elif option == 'goals':
            return db[0]    
        elif option == 'tutors':
            return db[1]
        elif option == 'days_of_week':
            return db[2]
        elif option == 'time_for_practice':
            return db[3]