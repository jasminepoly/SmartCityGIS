import os
from os.path import exists
import simplejson as json
import random
import  pprint as pprint
import numpy as np
from datetime import datetime
from random import randint
#ofdata
k=200

year="2018"
month=np.random.randint(low=1, high=4, size=(k,))
day=np.random.randint(low=1, high=28, size=(k,))
hour=np.random.randint(low=0, high=24, size=(k,))
minute=np.random.randint(low=0, high=60, size=(k,))
second=np.random.randint(low=0, high=60, size=(k,))

timestamp=[]
[timestamp.append(str(day[i])+"/"+str(month[i])+"/"+year+"T"+str(hour[i])+":"+str(minute[i])+":"+str(second[i])+"CET") for i in range(k)]


i=100 #number of sensors

longitude=np.random.uniform(low=36.6266, high=36.742, size=(i,))
latitude=np.random.uniform(low=2.752, high=3.2032, size=(i,))

json2= {"sensors":[{"sensor": "Station_Velib-"+str(j),
    "description": "Velibs disponibles",
    "type": "velib",
    "dataType": "number",
    "component": "Station_Velib-"+str(j),
    "componentType": "velib",
    "location": str(longitude[j])+" "+str(latitude[j]),
    "timeZone": "CET"}
                 for j in range (i)]}

data={"sensors":[{
        "sensor": "Station_Velib-"+ str(j),
        "observations":[
                {"value": randint(0,20),
                 "timestamp": timestamp[a],
                 "location": str(longitude[j])+" "+str(latitude[j])}
                for a in range(k) ]}
                                for j in range (i)]}
json2=json.dumps(json2)
data=json.dumps(data)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:482cd0273c1a54239baf9e8d464fd92f40c08c7c08c7c69f47d37108375dbac3\' -d \' " +json2+ " \' http://192.168.20.18:8081/catalog/ANT"
os.system(C)
M="curl -X PUT -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:482cd0273c1a54239baf9e8d464fd92f40c08c7c08c7c69f47d37108375dbac3\' -d \' " +data+ " \' http://192.168.20.18:8081/data/ANT"
os.system(M)
