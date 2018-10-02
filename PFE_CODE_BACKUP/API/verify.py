from sys import argv
import requests
import simplejson as json

headers={'Accept':'application/json'}
myUrl="http://192.168.20.13:8080/geoserver/rest/"
credential=('admin','geoserver')

#Get a json file that contains all the workspaces
def workspace_get():
        resp=requests.get(myUrl+"workspaces", auth= credential,headers=headers)
        workspaces= json.loads(resp.text)
        return workspaces
#Get a json file that contains all the datastores of a given workspace
def datastore_get(workspace_name):
        resp=requests.get(myUrl+"workspaces/"+workspace_name+"/datastores/", auth= credential,headers=headers)
        datastores= json.loads(resp.text)
        return datastores
#Get a json file that contains all the styles
def style_get():
        resp=requests.get(myUrl+"styles", auth= credential,headers=headers)
        styles= json.loads(resp.text)
        return styles

def layer_get():
        resp=requests.get(myUrl+"layers", auth= credential,headers=headers)
        layers= json.loads(resp.text)
        return layers
#if a workspace exist return 1 else return 0
def workspace_verify (workspace_name):
        workspaces= workspace_get()
        workspaces=workspaces['workspaces']['workspace']
        #check si workspace exist
        for i in range(len(workspaces)):
                k=workspaces[i]
                if k['name']==workspace_name:
                        return 1
                        break
        i=i+1
        if i==len(workspaces):
                return 0


#if a datastore exist return 1 else return 0
def datastore_verify(workspace_name,datastore_name):
        if (workspace_verify(workspace_name)==1):
                datastores=datastore_get(workspace_name)
                datastores=datastores['dataStores']['dataStore']
                for i in range(len(datastores)):
                        k=datastores[i]
                        if k['name']==datastore_name:
                                return 1
                                break
                i=i+1
                if i==len(datastores):
                        return 0
        else :
                return 0
#if a style exists return 1 else return 0
def style_verify(style_name):
        styles=style_get()
        styles=styles['styles']['style']
        for i in range(len(styles)):
                k=styles[i]
                if k['name']==style_name:
                        return 1
        i=i+1
        if i==len(styles):
                return 0

def layer_verify(layer_name):
        layers=layer_get()
        layers=layers['layers']['layer']
        for i in range(len(layers)):
                k=layers[i]
                if k['name']==layer_name:
                        return 1
                i=i+1
                if i==len(layers):
                        return 0
