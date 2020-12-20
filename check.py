
import requests


data=requests.get("https://restcountries.eu/rest/v2/",timeout=1.0)
res=data.json()
print(res[0])

