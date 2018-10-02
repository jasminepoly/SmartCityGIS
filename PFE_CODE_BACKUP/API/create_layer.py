#! usr/bin/env python
import time
import os
from sys import argv
from os.path import exists
import simplejson as json
import requests
import  geojson, gdal, subprocess
def create(layer):
        if (layer=='eau'):
                url = 'http://192.168.20.18:8081/data/Prov001?limit=5'
                headers={'IDENTITY_KEY':'193ae2c5b20dddc5d780747f60a1493978e0e0694f61d3c68cdad1e03615d911','content-type':'application/json'}

        if (layer=='poubelle'):
                url = 'http://192.168.20.18:8081/data/Prov002?limit=20'
                headers={'IDENTITY_KEY':'a46da1f689a7956aa9f39d2fb8540e5c810fa15096d0df7f806ea51c9557708c','content-type':'application/json'}

        r=requests.get(url,auth=('sentilo','sentilo'),headers=headers)
        data= r.text
        print data
        data=json.loads(data)
        lat=[]
        lon=[]
        i=0
        features=[]
        for d in data['sensors']:
                c=d["observations"][0]["location"].split("  ")
                lon.append(float(c[1]))
                lat.append(float(c[0]))

                for k in range (len(d['observations'])):
                        features.append({
                                "type": "Feature",
                                "geometry" : {
                                "type": "Point",
                                "coordinates": [lon[i], lat[i]],},
                                "properties" : d['observations'][k],
                                 })

                i=i+1
        geojson2 = {
                        "type": "FeatureCollection",
                        "features": features}


        print geojson2
        with open('data1.geojson', 'w') as f:
                geojson.dump(geojson2, f)
 args = ['ogr2ogr', '-f', 'ESRI Shapefile', layer+'.shp', 'data1.geojson']
        subprocess.Popen(args)
        time.sleep(.3)
        cmd='zip   data3.zip '+ layer+'.*'
        os.popen(cmd)
        time.sleep(.3)
        url = "http://192.168.20.13:8080/geoserver/rest/workspaces/sentilo/datastores/"+layer+"/file.shp"
        headers = {'content-type': 'application/zip'}
        with open('data3.zip', 'rb') as f:
          r=requests.put(url, data=f, headers=headers, auth=('admin','geoserver'))
        cmd="rm data3.zip"
        os.popen(cmd)
        print r.status_code
