# English-tutors-flask-app # Stepik project

Training project for [a course on the Stepik](<https://stepik.org/course/61900/>).
It's my second app on the Flask learning course. I make site of english language tutors.

Using dependencies: Flask + WTForms, Bootstrap 4. As a database I will use JSON file.
The site has:
* '/' - main page;
* '/all/' - page of all tutors;
* '/profiles/<tutor_id>/' - page of a certain tutor;
* '/goals/\<goal>/' - page with relevant tutors by certain goal;
* '/booking/<tutor_id>/<class_day>/\<time>/' - booking page and booking done page;
* '/request/' - page of request for mathing a relevant tutor and request done page;


< 🔻 *in progress* 🔻 >
* '/admin/' - admin's page with logging in for creating/editing/deleting tutors, goals and etc.;

To run this app, you should create date base first. So run create_json_db.py once.
