import requests

# API endpoint
url = "http://localhost:8000/register/"  # Replace with your actual API endpoint

# User data to send in the POST request
data = {
    "name": "test",
    "pwd": "test!@#",
    "email": "to@example.com"
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")