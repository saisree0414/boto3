import requests
from datetime import datetime

# Replace with your Artifactory URL and credentials
artifactory_url = 'https://your-artifactory-url'
username = 'your-username'
password = 'your-password'

# API endpoint to get all access tokens
api_url = f'{artifactory_url}/api/security/token'

# Create a session and authenticate with Artifactory
session = requests.Session()
session.auth = (username, password)

# Send GET request to retrieve all access tokens
response = session.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Iterate over each user and their access tokens
    for user in data:
        user_name = user['name']
        access_tokens = user['access_tokens']

        # Iterate over each access token
        for token in access_tokens:
            token_value = token['token_value']
            expires_in = token['expires_in']
            expiration_date = datetime.fromtimestamp(expires_in/1000)

            # Calculate the remaining days until token expiry
            remaining_days = (expiration_date - datetime.now()).days

            # Check if the token expires within the next 7 days
            if 0 < remaining_days <= 7:
                # Replace with your notification mechanism
                print(f"User: {user_name}")
                print(f"Token Value: {token_value}")
                print(f"Expiration Date: {expiration_date}")
                print(f"Remaining Days: {remaining_days}")
                print("Send notification here\n")
else:
    print(f"Request failed with status code {response.status_code}.")
