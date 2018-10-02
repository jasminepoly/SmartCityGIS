from sys import argv
import requests
import simplejson as json

headers={'Accept':'application/json'}
script, workspace = argv
myUrl='http://192.168.20.13:8080/geoserver/rest/workspaces/'
credential=('admin','geoserver')
resp=requests.get(myUrl, auth=credential,headers=headers)
workspaces= json.loads(resp.text)
workspaces=workspaces['workspaces']['workspace']
#check si workspace exist
headers={'Accept':'text/xml'}
for i in range(len(workspaces)):
        k=workspaces[i]
        if k['name']==workspace:
                print k['name']
                print myUrl+workspace
                resp = requests.delete(myUrl+workspace, auth=credential)
                print resp.status_code
                break

i=i+1
if i==len(workspaces):
        print "workspace " + workspace+" n'existe pas"