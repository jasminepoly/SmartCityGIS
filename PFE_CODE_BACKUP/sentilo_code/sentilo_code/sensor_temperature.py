import os
from os.path import exists
import simplejson as json
import random
import  pprint as pprint
import numpy as np
from datetime import datetime
from random import randint
#ofdata
k=1
etat=["Travaux_chaussee","Travaux_SEAAL","Travaux_SDA"]
year="2018"
month=np.random.randint(low=1, high=4, size=(k,))
day=np.random.randint(low=1, high=28, size=(k,))
hour=np.random.randint(low=0, high=24, size=(k,))
minute=np.random.randint(low=0, high=60, size=(k,))
second=np.random.randint(low=0, high=60, size=(k,))
i=0
timestamp=[]
[timestamp.append(str(day[i])+"/"+str(month[i])+"/"+year+"T"+str(hour[i])+":"+str(minute[i])+":"+str(second[i])+"CET") for i in range(k)]


i=7 #number of sensors

longitude=[36.36267,36.739,36.6,36.73,36.69,36.63,36.741]
latitude=[2.753,3,3.16,2.756,2.854,2.756,2.756]
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
#a=0
'''data={"sensors":[{
        "sensor": "Travaux-N"+ str(j),
        "observations":[
                {"value": random.choice(etat),
                 "timestamp": timestamp[a],
#                 "location": str(longitude[j])+" "+str(latitude[j])}
                for a in range(k) ]}
                                for j in range (i)]}'''
json2=json.dumps(json2)
#data=json.dumps(data)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:69d4481ebf8b08923014eee77ce4565d9393e057aaf36442b82f82f2e2c5a43d\' -d \' " +json2+ " \' http://192.168.20.18:8081/catalog/ANM"
os.system(C)
'''M="curl -X PUT -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:5f8377434043e6ed3d70c7fbeab65d4e3a3d83b74821f3dde4c61a541529c41c\' -d \' " +data+ " \' http://192.168.20.18:8081/data/ANTP"
os.system(M)'''
