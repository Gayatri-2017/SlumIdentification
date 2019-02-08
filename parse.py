'''https://gis.stackexchange.com/questions/73768/converting-geojson-to-python-objects
parse.py'''

import json

with open('test.json') as f:
    data = json.load(f)

for feature in data['features']:
    print feature['geometry']['type']
    print feature['geometry']['coordinates']
