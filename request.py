import requests
from collections.abc import Mapping

r = requests.post(url,json={'city':1, 'type':1, 'bhk':2})

print(r.json())