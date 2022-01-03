from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required=True,
    help="This field can't be left blank")

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item        
        return {"message":"Item not found"} ,404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'select * from items where  name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            item = {"item" :{"name":name,"price": row[1]}}
            return item,200
        return None


    def post(self, name):
        if self.find_by_name(name):
            return {"message": "item with name already exists"}
        
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?,?)" 
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()
        return item , 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return

    def put(self,name):
        
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items),None) 
        if item == None:
            item = {'name': name ,'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return items