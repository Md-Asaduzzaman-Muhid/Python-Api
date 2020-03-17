from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os



#Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/', methods = ['GET'])
def get():
	return jsonify({'you sent':"some_json"})


#Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

ma = Marshmallow(app)

# engine = SQLAlchemy('mysql://root:Muhid2277@localhost/prottasha_users')
# connection = engine.connect()

#Run Server
if __name__ == '__main__':
	app.run(debug=True)













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
