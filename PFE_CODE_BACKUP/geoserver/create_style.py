from sys import argv
import requests
import simplejson as json
headers={'Accept':'application/json'}
script, file_name,style= argv

url="http://192.168.20.13:8080/geoserver/rest/styles/"

payload =  '<style><name>'+style+'</name><filename>sentilo.sld</filename></style>'
headers = {'content-type': 'text/xml'}
r = requests.post(
    url,
    data=payload,
    headers=headers,
    auth=('admin','geoserver')
)
url= url+style


headers = {'content-type': 'application/vnd.ogc.sld+xml'}


with open(file_name, 'rb') as f:
    r = requests.put(
        url,
        data=f,
        headers=headers,
        auth=('admin','geoserver'))
