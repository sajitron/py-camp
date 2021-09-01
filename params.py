import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(url, headers={"Accept": "application/json"}, params={"term": "snow"})

data = response.json()

print(data["results"])