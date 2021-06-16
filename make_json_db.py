import data
import json


def copy_data_to_json():
    ''' 
    Due to the course requirements 
    1. I must use json file as a database
    2. I must copy info from data.py to json once 
    '''
    with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(
                (data.goals, data.teachers), 
                f, 
                ensure_ascii=False, 
                indent=4,
                separators=(',', ': ')
                )
                

if __name__ == '__main__':
    copy_data_to_json()