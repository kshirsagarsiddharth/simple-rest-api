import os 
import re 
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
uri = os.getenv('DATABASE_URL')
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://','postgresql://',1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)





api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/store')


if __name__ == "__main__":
    from db import db 
    db.init_app(app)
    app.run(debug=True)
