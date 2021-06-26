import json
import data, func


def make_json_db():
    ''' 
    Due to the course requirements 
    1. I must use json file as a database
    2. I must copy info from data.py to json once 
    '''
    with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(
                (data.goals, data.teachers, data.days_of_week, data.time_for_practice), 
                f, 
                ensure_ascii=False, 
                indent=4,
                separators=(',', ': '))   
                

if __name__ == '__main__':
    make_json_db()
    print()
    print('Database - db.json is successfully created')
    print()
    for tutor_id in [8, 9, 10, 11]: 
        func.add_goal_to_tutor('programming', tutor_id)
