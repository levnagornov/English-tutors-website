import json
from typing import Any, Union


def get_data_from_db(option: str = "all") -> dict[str, Any]:
    """Read data from database (``db.json``) and returns a ``dict`` of data.
    1. Mode by default is ``option='all'`` returns dict with all data.
    2. ``option='tutors'`` returns dict with only about tutors.
    3. ``option='goals'`` returns dict with only about goals.
    4. ``option='days_of_week'`` returns dict with days of the week in rus and eng
    5. ``option='time_for_practice'`` returns dict with days.
    """
    if option not in ("all", "tutors", "goals", "days_of_week", "time_for_practice"):
        raise AttributeError

    with open("db.json", encoding="utf-8") as f:
        db: list[Union[list, dict]] = json.load(f)
        if option == "all":
            return db
        elif option == "goals":
            return db[0]
        elif option == "tutors":
            return db[1]
        elif option == "days_of_week":
            return db[2]
        elif option == "time_for_practice":
            return db[3]


def is_tutor_free(tutor_info: dict, class_day: str, time: str) -> bool:
    """Checks if certain ``tutor`` is able to take a class in certain ``class_day`` and ``time``."""

    possible_days_of_week: dict = get_data_from_db(option="days_of_week")
    if class_day not in possible_days_of_week:
        return False

    day_schedule: dict = tutor_info["free"].get(
        class_day[:3], {}
    )  # we cut class_day to 3 letters, cause in db.json the keys in tutors schedule have 3 letter like 'mon', 'tue'
    if day_schedule.get(time):
        return True

    return False


def add_goal_to_tutor(goal: str, tutor_id: int) -> None:
    """Appends a ``goal`` to a tutor goals by ``tutor_id`` in database (``db.json``)."""

    with open("db.json", encoding="utf-8") as f:
        db: list = json.load(f)
        all_tutors: list = db[1]
        for tutor_info in all_tutors:
            if tutor_info["id"] == tutor_id:
                if goal not in tutor_info["goals"]:
                    tutor_info["goals"].append(goal)

    with open("db.json", "w", encoding="utf-8") as w:
        json.dump(db, w, ensure_ascii=False, indent=4, separators=(",", ": "))


def save_request(request: Any, file_name: str) -> None:
    """Saves ``request`` into file with ``file_name``."""

    try:
        with open(file_name, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    data.append(request)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, separators=(",", ": "))
