from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'a store with name {} already exists.'.format(name)}

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            {'message': 'an error occurered while creating the store'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        stores = StoreModel.get_stores_list()
        return {'stores': [store.json() for store in stores]}
