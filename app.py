from flask import Flask, request
from flask_restful import  Api
from flask_jwt import JWT

from security import authenicate, identity

from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'Secret'
api = Api(app)

jwt = JWT(app,authenicate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/user')

app.run(port=5000,debug=True)