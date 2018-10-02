from sys import argv
import requests
import simplejson as json

headers={'Accept':'application/json'}
script, workspace,datastore = argv
myUrl='http://192.168.20.13:8080/geoserver/rest/workspaces/'
credential=('admin','geoserver')
resp=requests.get(myUrl, auth=credential,headers=headers)
workspaces= json.loads(resp.text)
workspaces=workspaces['workspaces']['workspace']
#check si workspace exist
for i in range(len(workspaces)):
        k=workspaces[i]
        if k['name']==workspace:
                print k['name']
                try:
                        mode=int(raw_input('1-postgres    2- shapefile:   '))
                except ValueError:
                        print "Not a number"
                if mode==1:
                        data='<dataStore><name>'+datastore+'</name><connectionParameters><host>192.168.20.13</host> <port>5432</port><database>sentilo</database><schema>public</schema><user>sentilo1</user><passwd>masmine1994</passwd><dbtype>postgis</dbtype></connectionParameters></dataStore>'
                        url=myUrl+workspace+'/datastores/'
                        headers = {'content-type': 'text/xml','Accept': 'text/xml'}
                        r=requests.post(url, data=data, headers=headers, auth=credential)
                if mode ==2:
                        url=myUrl+workspace+'/datastores/'+datastore+'/file.shp'
                        headers = {'content-type': 'application/zip'}
                        try:
                                file_name=raw_input('lien au dossier zip: ')
                        except ValueError:
                                print "dossier n'existe pas"
                        with open(file_name, 'rb') as f:
                                r=requests.put(url, data=f, headers=headers, auth=('admin','geoserver'))
                                print r.status_code
                break

i=i+1
if i==len(workspaces):
        print "workspace " + workspace+" n'existe pas"
