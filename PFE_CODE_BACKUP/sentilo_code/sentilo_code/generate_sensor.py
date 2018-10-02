import os
from os.path import exists
import simplejson as json
import random
import  pprint as pprint
import numpy as np

i=8 #number of sensors

longitude=[36.60507,36.66138,36.8678,36.64078,36.69914,36.58791,36.714170,36.788722]
latitude=[3.11,2.88254,2.77954,2.93541,2.9512,2.95052,3.021964,3.015700]

j=0
json2= {"sensors":[{"sensor": "temperature-"+str(j+1),
    "description": "Temperature ambiante",
    "type": "temperature",
    "dataType": "number",
    "unit":"C",
    "component":"temperature-"+str(j+1),
    "componentType": "temperature",
    "location": str(longitude[j])+" "+str(latitude[j]),
    "timeZone": "CET"}
                 for j in range (i)]}
j=0
json2=json.dumps(json2)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:69d4481ebf8b08923014eee77ce4565d9393e057aaf36442b82f82f2e2c5a43d\' -d \' " +json2+ " \' http://192.168.20.18:8081/catalog/ANM"
os.system(C)
