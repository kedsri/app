import json
import requests

url="http://api.open-notify.org/astros.json"
print(url)
response=requests.get(url)
print("response is:" + str(response))
resp_json=str(response.json())
print("resp_json is "+str(resp_json))
#read_json=json.loads(str(response))
print("json index.." +resp_json.index(5))
if resp_json[11]=="Dmitry Petelin":
   print("parsed..")
print ("???" + json.dumps(resp_json))