import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'inputs':[10000,1212,19,50850,0.130348259,5.3],})
print(r.json())
