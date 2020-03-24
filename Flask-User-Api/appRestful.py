from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Muhid2277@localhost/prottasha_users'
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column('id', db.Integer, primary_key= True)
	name = db.Column('name', db.String(50))
	email = db.Column('email', db.String(50))
	phone = db.Column('phone', db.String(25))


class Hello(Resource):
	def get(self):
		return {'Hello' : "db"}
	def post(self):
		some_jeson = request.get_json()
		return {'You Sent' : some_jeson}, 201

api.add_resource(Hello,'/')

if __name__ == '__main__':
	app.run(debug = True)