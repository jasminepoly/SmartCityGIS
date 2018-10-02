#! usr/bin/env python
import os
from os.path import exists
import simplejson as json
import random
import  pprint as pprint
json2= {"sensors":[{"sensor": "Bus-"+str(j),
    "description": "Arret de bus",
    "type": "bus",
    "dataType": "text",
    "component": "Bus-"+str(j),
    "componentType": "bus",
    "location": str(random.uniform(36.6266,36.742))+" "+str(random.uniform(2.752,3.2032)),
    "timeZone": "CET"} for j in range (0,200 )]}
k=json.dumps(json2)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY: 482cd0273c1a54239baf9e8d464fd92f40c08c7c08c7c69f47d37108375dbac3\' -d \' " +k+ " \' http://192.168.20.18:8081/catalog/ANT"
os.system(C)
