import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

print(response.json())