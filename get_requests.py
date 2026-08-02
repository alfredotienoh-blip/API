import requests
# Making a get request to the specified URL
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.content)  # Print the raw content of the response