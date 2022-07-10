# Register imports
from flask import Flask, request, jsonify
from models import db
from models import Client
from config import config
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
import os

#App startup configuration
def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
   
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

enviroment = config['development']
if os.environ.get('PRODUCTION', default=False):
    enviroment = config['production']
    
app = create_app(enviroment)

#Schema registration and configuration
ma = Marshmallow(app)

class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'email', 'basic', 'full', 'date')

client_schema = ClientSchema()  #Schema instance for only one record
clients_schema = ClientSchema(many=True)  #Schema instance for multiple records

#CORS instance
CORS(app)


#GET request to get all the records
@cross_origin
@app.route('/client', methods=['GET'])
def get_clients():
    try:
        all_clients = Client.query.all()
        result = clients_schema.dump(all_clients)
        return clients_schema.jsonify(result)
    except Exception as ex:
        return jsonify({'message': 'error obteniendo los registros'})

#GET request with ID to get only one record
@app.route('/client/<id>', methods=['GET'])
def get_client(id):
    try:
        result = Client.query.get(id)
        return client_schema.jsonify(result)
    except Exception as ex:
        return jsonify({'message': "error obteniendo el registro a editar"})

#POST request to send a record
@app.route('/client', methods=['POST'])
def save_client():
    try:
        name = request.json['name']
        phone = request.json['phone']
        email = request.json['email']
        basic = request.json['basic']
        full = request.json['full']
        date = request.json['date']
        result = Client(name, phone, email, basic, full, date)
        db.session.add(result)
        db.session.commit()
        return jsonify({'message':'Cliente registrado', 'type':'success'})
    except Exception as ex:
        return jsonify({'message':'error enviando nuevo registro', 'type':'error'})

#PUT request with ID for updating a record
@app.route('/client/<id>', methods=['PUT'])
def update_client(id):
    try:
        result = Client.query.get(id)
        name = request.json['name']
        phone = request.json['phone']
        email = request.json['email']
        basic = request.json['basic']
        full = request.json['full']
        date = request.json['date']
        result.name = name
        result.phone = phone
        result.email = email
        result.basic = basic
        result.full = full
        result.date = date
        db.session.commit()
        return jsonify({'message':'Cliente Actualizado', 'type':'success'})
    except Exception as ex:
        return jsonify({'message':'error enviando registro editado', 'type':'error'})

#DELETE request with ID to delete a record
@app.route('/client/<id>', methods=['DELETE'])
def delete_client(id):
    try:
        result = Client.query.get(id)
        db.session.delete(result)
        db.session.commit()
        return jsonify({'message':'Cliente Eliminado', 'type':'success'})
    except Exception as ex:
        return jsonify( {'message': 'error eliminando registro', 'type': 'error'} )


#Start app
if __name__=='__main__':
    app.run()