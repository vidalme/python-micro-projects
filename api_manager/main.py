import requests

url = "https://randomfox.ca/floof"

response = requests.get(url)

# print(response.status_code)
# print(response.text)

fox = response.json()
print(fox['image'])