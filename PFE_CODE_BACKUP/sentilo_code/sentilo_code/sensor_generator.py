#! usr/bin/env python
import os
from os.path import exists
import simplejson as json 
import random
import  pprint as pprint
json2= {"sensors":[{"sensor": "Temperature-"+str(j),
    "type": "",
    "dataType": "number",
    "unit": "%",
    "component": "Poubelle-"+str(j),
    "componentType": "poubelle",
    "location": str(random.uniform(36.6266,36.742))+" "+str(random.uniform(2.752,3.2032)),
    "timeZone": "CET"} for j in range (20,200 )]}
k=json.dumps(json2)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY: 0f02ec8fcb720ffc9063165b6de94ad6992c52e2d10b7910ebbc7c96fa23cb4e\' -d \' " +k+ " \' http://192.168.20.18:8081/catalog/AND"
os.system(C)
