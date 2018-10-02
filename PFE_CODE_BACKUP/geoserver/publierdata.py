#! usr/bin/env python
from sys import argv
import os
from os.path import exists

import requests
script, file_name, datastore, vis=argv

args='shp2pgsql -c -D -I  '+ file_name +'   '+datastore+'  | PGPASSWORD=masmine1994  psql -d opendata -h 192.168.20.13 -U opendata'
print args
os.popen(args)
url='http://192.168.20.13:8080/geoserver/rest/workspaces/opendata/datastores'
'''
headers = {'content-type': 'text/xml'}
auth=('admin','geoserver')
data='<dataStore><name>'+datastore+'</name> <connectionParameters><host>192.168.20.13</host><port>5432</port><database>opendata</database><schema>public</schema><user>opendata</user><passwd>masmine1994</passwd><dbtype>postgis</dbtype></connectionParameters</dataStore>'

r=requests.post(url,headers=headers,auth=auth,data=data)
print r.status_code
args='curl -u admin:geoserver -v -XPOST -H "Content-Type:text/xml" -T datastore.xml http://192.168.20.13:8080/geoserver/rest/workspaces/sentilo/datastores'
os.popen(args)
'''
data='<dataStore><name>'+datastore+'</name><connectionParameters><host>192.168.20.13</host> <port>5432</port><database>opendata</database><schema>public</schema><user>opendata</user><passwd>masmine1994</passwd><dbtype>postgis</dbtype></connectionParameters></dataStore>'
credential=('admin','geoserver')
headers = {'content-type': 'text/xml','Accept': 'text/xml'}
r=requests.post(url, data=data, headers=headers, auth=credential)

print r.status_code
