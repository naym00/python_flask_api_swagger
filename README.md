# python_flask_api_swagger

From this project you can get hotel data in format of json using combination of these parameters Hotel name, price, location, ratting, Amminities.<br />
You can sort also by typing asc or desc in the sort_by_price field.  <br />
Authentication Part: Hit this link ```http://127.0.0.1:5000/``` Click on post and type email ```nymur@w3engineers.com``` password ```admin```<br />
Then you will get a token which is valid for 30 min.<br />
After then to have json data click on get and paste token like this format ```Bearer your_token.<br />
Then fullfill other fields.

### Prerequisite
- [x] Install Python
- [x] Install XAMPP 

## Step 1 Database:
- [x] Create a database named in hotel_database and then import hotel_database.sql<br />
Note: If the hotel_database.sql doesn't work then create table using the query bellow
```
CREATE TABLE hotel_database.hotel_information (
  id int(11) NOT NULL AUTO INCREMENT,
  location varchar(255) NOT NULL,
  hotel_name varchar(500) NOT NULL,
  rating varchar(20) DEFAULT NULL,
  stars varchar(50) DEFAULT NULL,
  cost varchar(50) DEFAULT NULL,
  facility varchar(500) DEFAULT NULL,
  url varchar(500) DEFAULT NULL
);
```
## Step 2:
- [x] virtualenv venv
## Step 3:
- [x] source venv/bin/activate
## Step 4:
##### Once you have activated your environment, install this packages.
- [x] pip install flask
- [x] pip install flask_swagger_ui
- [x] pip install mysql-connector-python
- [x] pip install Flask-JWT-Extended
- [x] pip install flasgger
## Step 5:
##### while virtual environment is activated then tell Flask where to find the application (app.py in your case) using the FLASK_APP environment variable with the following command.
- [x] export FLASK_APP=app
## Step 6:
##### Then specify that you want to run the application in development mode (so you can use the debugger to catch errors) with the FLASK_ENV environment variable.
- [x] export FLASK_ENV=development
## Step 7:
- [x] pip install -r requirements.txt python3 app.py
## Step 8:
- [x] To run the project ```flask run```
