from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result.data)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)


# from flask import Flask, render_template,jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os

# app = Flask(__name__)

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


######
######


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











