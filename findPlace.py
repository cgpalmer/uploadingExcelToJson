import json


f = open('placeToVisitInEdinburgh.json',)
data = json.load(f)

for p in data['placesToVisit']:
    print(p['place'])

placeId = 2
chosenPlace = []

if placeId in data:
    chosenPlace.append(data[placeId])
    print(chosenPlace)