# patient-provider-API
A Python-flask web API service for managing doctors and their schedules, enables patients to schedule appointment with patient providers.


# Design introduction #
I use the Python flask web framework to build a web application that can:
1. CRUD doctor information (two address locations are available for each doctor and this is for the internal use)
2. Show all the available appointments of all doctors at all locations 3. Make and cancel the appointment with the doctor.
4. If you make the appointment with a doctor at a certain time at the certain location, the doctor will be unavailable for that certain time and location.
5. Log-in function for the internal users to input doctor information is not available at this time, since it requires preset databases. So right now, anyone can edit the doctor information.


# To run the API #
1. Have Python2.7, pip, Flask-MySQL installed.

2. Install Flask-MySQL:
    > pip install flask-mysql 
    http://flask-mysql.readthedocs.io/en/latest/#installation 

3. Database preparation:

  a. Config database: I use the ‘localhost’ with user name ‘root’ and password ‘123456’. If your database setup is different, you need to change the database config under manage.py (line 13).

  b. To connect to MySQL server:
    > mysql -u root -p

  c. Execute the config file to set up the database tables:
    mysql> SOURCE [PATH of DIRECTORY]/config.sql

4. run the manage.py to run the server:
    > python manage.py runserver

5. Running on localhost http://127.0.0.1:5000/
