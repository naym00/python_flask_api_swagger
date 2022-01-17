from tempfile import template
import flask
from flask import Flask, jsonify, request, make_response, redirect,render_template
from flasgger import Swagger,swag_from
from mysql.connector import cursor
import mysql.connector
from static.swagger import swagger_config,template
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta

import json
app = Flask(__name__)
app.config['DEBUG'] = True

db_connector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel_database"
    )
cursor = db_connector.cursor()

JWTManager(app)

app.config.from_mapping(
            
            JWT_SECRET_KEY =("secretkey"),
            SWAGGER = {
                "title" : "Hotel Api",
                "uiversion" : 3
            }
        )

Swagger(app, config=swagger_config, template=template)

@app.post('/resources/v1/login')
@swag_from('./static/login.yaml')
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if email == 'nymur@w3engineers.com' and password == 'admin':
        token = create_access_token(identity= email, expires_delta=timedelta(minutes=30))
        return jsonify({'token': token})
  
    else:
        return 'Invalid Credentials. Please try again.'
        

@app.get('/resources/v1/hotels')
@jwt_required()
@swag_from('./static/hotel.yaml')
def resources():
    user_email = get_jwt_identity()
    if user_email == 'nymur@w3engineers.com':
        hotels = []
        sql = ''

        title_ = location_ = price_ = amenities_ = False
        if request.args.get('title') != None:
            title_ = True
        if request.args.get('amenities') != None:
            amenities_ = True
        if request.args.get('price') != None:
            price_ = True
        if request.args.get('location') != None:
            location_ = True
            
        if title_ == True and amenities_ == True and price_ == True and location_ == True:
            title_value = request.args.get('title')
            amenities_value = request.args.get('amenities')
            price_value = request.args.get('price')
            location_value = request.args.get('location')         
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and facility LIKE' + f'"%{amenities_value}%"' + ' and cost=' + f'"{price_value}"' + ' and location=' + f'"{location_value}"' 
        elif title_ == True and amenities_ == True and price_ == True and location_ == False:
            title_value = request.args.get('title')
            amenities_value = request.args.get('amenities')
            price_value = request.args.get('price')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and facility LIKE' + f'"%{amenities_value}%"' + ' and cost=' + f'"{price_value}"'

        elif title_ == True and amenities_ == True and price_ == False and location_ == True:
            title_value = request.args.get('title')
            amenities_value = request.args.get('amenities')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and facility LIKE' + f'"%{amenities_value}%"' + ' and location=' + f'"{location_value}"'

        elif title_ == True and amenities_ == True and price_ == False and location_ == False:
            title_value = request.args.get('title')
            amenities_value = request.args.get('amenities')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and facility LIKE' + f'"%{amenities_value}%"'

        elif title_ == True and amenities_ == False and price_ == True and location_ == True:
            title_value = request.args.get('title')
            price_value = request.args.get('price')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and cost=' + f'"{price_value}"' + ' and location=' + f'"{location_value}"'

        elif title_ == True and amenities_ == False and price_ == True and location_ == False:
            title_value = request.args.get('title')
            price_value = request.args.get('price')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and cost=' + f'"{price_value}"' 

        elif title_ == True and amenities_ == False and price_ == False and location_ == True:
            title_value = request.args.get('title')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"' + ' and location=' + f'"{location_value}"'

        elif title_ == True and amenities_ == False and price_ == False and location_ == False:
            title_value = request.args.get('title')
            sql='SELECT * FROM hotel_information WHERE hotel_name=' + f'"{title_value}"'

        elif title_ == False and amenities_ == True and price_ == True and location_ == True:
            amenities_value = request.args.get('amenities')
            price_value = request.args.get('price')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE facility LIKE' + f'"%{amenities_value}%"' + ' and cost=' + f'"{price_value}"' + ' and location=' + f'"{location_value}"'

        elif title_ == False and amenities_ == True and price_ == True and location_ == False:
            amenities_value = request.args.get('amenities')
            price_value = request.args.get('price')
            sql='SELECT * FROM hotel_information WHERE facility LIKE' + f'"%{amenities_value}%"' + ' and cost=' + f'"{price_value}"'

        elif title_ == False and amenities_ == True and price_ == False and location_ == True:
            amenities_value = request.args.get('amenities')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE facility LIKE' + f'"%{amenities_value}%"' + ' and location=' + f'"{location_value}"'

        elif title_ == False and amenities_ == True and price_ == False and location_ == False:
            amenities_value = request.args.get('amenities')
            sql='SELECT * FROM hotel_information WHERE facility LIKE' + f'"%{amenities_value}%"'

        elif title_ == False and amenities_ == False and price_ == True and location_ == True:
            price_value = request.args.get('price')
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE cost=' + f'"{price_value}"' + ' and location=' + f'"{location_value}"'
            
        elif title_ == False and amenities_ == False and price_ == True and location_ == False:
            price_value = request.args.get('price')
            sql='SELECT * FROM hotel_information WHERE cost=' + f'"{price_value}"'

        elif title_ == False and amenities_ == False and price_ == False and location_ == True:
            location_value = request.args.get('location')
            sql='SELECT * FROM hotel_information WHERE location=' + f'"{location_value}"'

        if sql == '':
            return jsonify({'message': 'Please insert combination of these or any of these title, amenities, price, location'})
        query=sql
        cursor.execute(query)
        results = cursor.fetchall()


        for x in results:
            data = {'id': x[0], 'location': x[1], 'hotel_name': x[2], 'rating': float(x[3]), 'stars': int(x[4]), 'cost': int(x[5].replace(",","")), 'facility': x[6], 'url': x[7]}
            hotels.append(data)
        if request.args.get('sort_by_price') == 'asc':
            hotels.sort(key=lambda x: x['cost'])
        elif request.args.get('sort_by_price') == 'desc':
            hotels.sort(key=lambda x: x['cost'], reverse=True)
        return jsonify(hotels)
       
app.run()