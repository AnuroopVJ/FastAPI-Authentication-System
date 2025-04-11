import requests

# API endpoint for OTP verification
url = "http://localhost:8000/otp/"  # Replace with your actual API endpoint

# OTP data to send in the POST request
data = {
    "otp": "1234", 
    "email": "to@example.com",
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")