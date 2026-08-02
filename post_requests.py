import requests
# Making a post request to the specified URL with JSON data
data = {
    "name": "John Doe", 
    "email": "john.doe@example.com"
}
response = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
print(response.content)  # Print the raw content of the response