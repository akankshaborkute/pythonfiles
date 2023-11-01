import requests
response=requests.get('http://api.open-notify.org/astros.json')
json=response.json()
print("People  currently in space are",json)
for person in json['people']:
    print(person)

for person in json['people']:
    print(person['name'])

