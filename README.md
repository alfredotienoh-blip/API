# API
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print(response.json())
print(response.text)
data = response.json()
print(data["name"])

import requests
# Making a post request to the specified URL with JSON data
data = {
    "name": "John Doe", 
    "email": "john.doe@example.com"
}
response = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
print(response.content)  # Print the raw content of the response
