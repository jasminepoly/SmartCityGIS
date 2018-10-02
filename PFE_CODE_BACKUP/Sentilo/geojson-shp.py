from sys import argv
from os.path import exists

import urllib, geojson, gdal, subprocess
script, in_file = argv
donne=open(in_file)
data = geojson.loads(donne.read())

with open('data.geojson', 'w') as f:
    geojson.dump(data, f)

args = ['ogr2ogr', '-f', 'ESRI Shapefile', 'destination_data.shp', 'data.geojson']
subprocess.Popen(args)
