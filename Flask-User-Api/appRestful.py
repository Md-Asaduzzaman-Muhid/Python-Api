from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
	def get(self):
		return {'Hello' : 'World'}
	def post(self):
		some_jeson = request.get_json()
		return {'You Sent' : some_jeson}, 201

api.add_resource(Hello,'/')

if __name__ == '__main__':
	app.run(debug = True)