from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql://root:Muhid2277@localhost/prottasha_users')
engine.execute('CREATE TABLE "EX1" ('
               'id INTEGER NOT NULL,'
               'name VARCHAR, '
               'PRIMARY KEY (id));')
# from flask import Flask, render_template,jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os



# #Init App
# app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))


# @app.route('/', methods = ['GET'])
# def get():
# 	return jsonify({'you sent':"some_json"})


# #Database 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Muhid2277@localhost/prottasha_users'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# db = SQLAlchemy(app)

# ma = Marshmallow(app)

# class Employee(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	username = db.Column(db.String(60), unique = True)
# 	email = db.Column(db.String(60), unique = True)

# # engine = SQLAlchemy('mysql://root:Muhid2277@localhost/prottasha_users')
# # connection = engine.connect()

# def __init__(self,username,email):
# 	self.username = username
# 	self.email = email

# #Run Server
# if __name__ == '__main__':
# 	app.run(debug=True)











# @app.route('/', methods = ['GET','POST'])
# def index():
# 	if(request.method == 'POST'):
# 		some_json = request.get_json()
# 		return jsonify({'you sent':some_json}),201
# 	else:
# 		return jsonify({'about':"Hollo World"})
# @app.route('/multi/<int:num>', methods= ["GET"])
# def get_multiply10(num):
# 	return jsonify({'result': num*10})

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0')
