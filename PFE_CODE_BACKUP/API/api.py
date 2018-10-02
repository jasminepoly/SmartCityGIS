from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import verify as vrf
import sentilo_geoserver as sg

app = Flask(__name__)
api = Api(app)

class Verify_workspace(Resource):
    def get(self):
        return vrf.workspace_get()

class Verify_datastore(Resource):
    def get(self, todo):
        return vrf.datastore_get(todo) # Fetches first column that is Employee ID

class Verify_layer(Resource):
    def get(self):
        return vrf.layer_get() # Fetches first column that is Employee ID

class Fond_de_plan(Resource):
    def get(self):
        return "OK" # Fetches first column that is Employee ID

class Capteur(Resource):
    def get(self, capteur_id):
        print(vrf.layer_verify(capteur_id))
        if vrf.layer_verify(capteur_id)==1:
                return "Layer exists"
        else:
            sg.create(capteur_id)
            return "Layer created in geoserver"

api.add_resource(Verify_workspace, '/Verify_workspace') # Route_1
api.add_resource(Verify_datastore, '/Verify_datastore/<todo>') # Route_2
api.add_resource(Verify_layer, '/Verify_layer') # Route_3
api.add_resource(Fond_de_plan, '/Fond_de_plan') # Route_4
api.add_resource(Capteur, '/capteur/<capteur_id>') # Route_5

if __name__ == '__main__':
     app.run(host="192.168.20.18",port=0101,debug=True)
