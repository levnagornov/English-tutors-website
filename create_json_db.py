""" 
Due to the course requirements 
1. I must use json file as a database;
2. I must copy date from data.py to db.json only once;
3. I must add additional goal to some tutors;
"""

import json, os

import data, func


def create_json_db(*args) -> None:
    """
    Creates db.json file in current directory with included *args objects.
    """
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(args, f, ensure_ascii=False, indent=4, separators=(",", ": "))


if __name__ == "__main__":
    # create db if not exists
    if not os.path.exists("db.json"):
        create_json_db(
            data.goals, data.teachers, data.days_of_week, data.time_for_practice
        )
        print("\nDatabase - db.json is successfully created\n")

    # add a new goal 'programming' for some tutors
    for tutor_id in [8, 9, 10, 11]:
        func.add_goal_to_tutor("programming", tutor_id)
