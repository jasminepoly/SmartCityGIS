from sys import argv
import requests
import simplejson as json
headers={'Accept':'application/json'}
script, workspace= argv
myUrl="http://192.168.20.13:8080/geoserver/rest/workspaces"
credential=('admin','geoserver')
resp=requests.get(myUrl, auth= credential,headers=headers)
workspaces= json.loads(resp.text)
workspaces=workspaces['workspaces']['workspace']
#check si workspace exist
for i in range(len(workspaces)):
        k=workspaces[i]
        print k['name']
        if k['name']==workspace:
                print "workspace existe deja"
                break
i=i+1
#Creation de Workspace
headers={"Content-type": "text/xml"}
if i==len(workspaces):
        workspace_xml="<workspace><name>"+workspace+"</name></workspace>"
        print workspace_xml
        t=requests.post(myUrl, auth=credential,data=workspace_xml,headers=headers)
        print t.status_code