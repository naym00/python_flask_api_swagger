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

## Step 1:
- [x] create a database named in hotel_database and then import hotel_database.sql
- [x] virtualenv venv
## Step 2:
- [x] source venv/bin/activate
## Step 3:
##### Once you have activated your environment, install this packages.
- [x] pip install flask
- [x] pip install flask_swagger_ui
- [x] pip install mysql-connector-python
- [x] pip install Flask-JWT-Extended
- [x] pip install flasgger
## Step 4:
- [x] export FLASK_APP=app
- [x] export FLASK_ENV=development
## Step 5:
- [x] pip install -r requirements.txt python3 app.py
## Step 6:
- [x] flask run

