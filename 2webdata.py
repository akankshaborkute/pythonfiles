import json
import requests
import sys
print(len(sys.argv))
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])   
# print(json.dumps(response.json(),indent=2))
o=response.json()
for result in o["results"]:
    print(result["trackName"])



# responce=requests.get("https://www.python.org")   
# print(responce.status_code)
# responce=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer") 
# print(responce.json())