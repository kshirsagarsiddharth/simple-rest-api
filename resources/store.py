from flask_restful import Resource 
from models.store import StoreModel 

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name = name)  
        if store:
            return store.json(), 200 
        return {'message':'Store not found'}, 404 

    def post(self,name):
        if StoreModel.find_by_name(name = name):
             return {'message':f'A store with {name} already exists'}, 400 
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occured while creating the store'}, 500 
        return store.json(), 201 


    def delete(self, name):
        store = StoreModel.find_by_name(name = name) 
        if store:
            store.delete_from_db()
        return {'message':'Store Deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores':list(map(lambda x : x.json(), StoreModel.query.all()))}
        
    
