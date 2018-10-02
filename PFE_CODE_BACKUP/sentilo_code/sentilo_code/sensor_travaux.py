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


i=70 #number of sensors

longitude=np.random.uniform(low=36.6266, high=36.742, size=(i,))
latitude=np.random.uniform(low=2.752, high=3.2032, size=(i,))
j=0
json2= {"sensors":[{"sensor": "Travaux-N"+str(j),
    "description": "Travaux en cours",
    "type": "travaux",
    "dataType": "text",
    "component":"Travaux-N"+str(j),
    "componentType": "travaux",
    "location": str(longitude[j])+" "+str(latitude[j]),
    "timeZone": "CET"}
                 for j in range (50,70)]}
j=0
a=0
data={"sensors":[{
        "sensor": "Travaux-N"+ str(j),
        "observations":[
                {"value": random.choice(etat),
                 "timestamp": timestamp[a],
                 "location": str(longitude[j])+" "+str(latitude[j])}
                for a in range(k) ]}
                                for j in range (50,70)]}
json2=json.dumps(json2)
data=json.dumps(data)
C="curl -X POST -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:5f8377434043e6ed3d70c7fbeab65d4e3a3d83b74821f3dde4c61a541529c41c\' -d \' " +json2+ " \' http://192.168.20.18:8081/catalog/ANTP"
os.system(C)
M="curl -X PUT -H \'Content-Type: application/json\' -H \'IDENTITY_KEY:5f8377434043e6ed3d70c7fbeab65d4e3a3d83b74821f3dde4c61a541529c41c\' -d \' " +data+ " \' http://192.168.20.18:8081/data/ANTP"
os.system(M)
