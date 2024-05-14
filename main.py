import requests
import base64

# Set your consumer key and secret
consumer_key = "MIML_AyI_Xadnb0MBJHCJ0VA7jca"
consumer_secret = "HbNirWqfRNXOloew_TbTDdvOW0Ua"

# Concatenate consumer key and secret with a colon
credentials = f"{consumer_key}:{consumer_secret}"

# Encode credentials in Base64
credentials_encoded = base64.b64encode(credentials.encode()).decode()

# Define token endpoint and parameters
token_endpoint = "https://napi.kotaksecurities.com/oauth2/token"
data = {
    "grant_type": "client_credentials",
    # Add any additional parameters required by the API
}

# Define headers with Authorization
headers = {
    "Authorization": f"Basic {credentials_encoded}",
    "Content-Type": "application/json",
}

# Send POST request to get access token
response = requests.post(token_endpoint, headers=headers, json=data)

# Check if request was successful
if response.status_code == 200:
    # Parse response to get access token
    access_token = response.json().get("access_token")
    print("Access Token:", access_token)
else:
    print("Error occurred:", response.text)

