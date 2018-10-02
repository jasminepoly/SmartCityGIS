#! usr/bin/env python
import os
from sys import argv
from os.path import exists
import simplejson as json
import requests
import  geojson, gdal, subprocess
script,file_name, datastore=argv
cmd ='curl -X GET  -H "IDENTITY_KEY:193ae2c5b20dddc5d780747f60a1493978e0e0694f61d3c68cdad1e03615d911" -H "Content-Type: application/json"  http://192.168.20.18:8081/data/Prov001/EAU?limit=20'
data=os.popen(cmd).read()
data=json.loads(data)
data= data["observations"]
i=0
lat=[]
lon=[]
for d in data:
        c=d['location'].split(' ')
        lon.append(float(c[0]))
        lat.append(float(c[1]))
        i=i+1
geojson2 = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [lon[j], lat[j]],
            },
        "properties" : d,
     } for j in range(i)]
}

with open('data1.geojson', 'w') as f:
    geojson.dump(geojson2, f)

args = ['ogr2ogr', '-f', 'ESRI Shapefile', 'sentilo_points.shp', 'data1.geojson']
subprocess.Popen(args)

cmd='zip '+ file_name+ '  sentilo_points.*'
print (cmd)
os.popen(cmd)
url = "http://192.168.20.13:8080/geoserver/rest/workspaces/sentilo/datastores/"+datastore+"/file.shp" 
headers = {'content-type': 'application/zip'}

cmd="rm sentilo_points.*"
os.popen(cmd)
with open(file_name, 'rb') as f:
	r=requests.put(url, data=f, headers=headers, auth=('admin','geoserver'))


cmd="rm " + file_name
os.popen(cmd)
print r.status_code

