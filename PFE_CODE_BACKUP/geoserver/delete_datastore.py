from sys import argv

import requests
import simplejson as json

headers={'Accept':'application/json'}
script, workspace, datastore = argv
myUrl='http://192.168.20.13:8080/geoserver/rest/workspaces/'+workspace+'/datastores/'
credential=('admin','geoserver')
resp=requests.get(myUrl, auth=credential,headers=headers)
datastores= json.loads(resp.text)
datastores=datastores['dataStores']['dataStore']
#check si workspace exist
for i in range(len(datastores)):
        k=datastores[i]
        if k['name']==datastore:

                r=requests.get(myUrl+datastore, auth=credential,headers=headers)
                url=myUrl+datastore+'?recurse=true'
                resp = requests.delete(url,auth=credential,headers=headers)
                print datastore+ ' a ete supprime'
                break
i=i+1
if i==len(datastores):
        print "datastore " + datastore+" n'existe pas"
