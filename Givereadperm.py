import requests

# Replace these variables with your Artifactory instance details
artifactory_url = "https://your-artifactory-instance-url"
api_key = "your-api-key-or-username"
permission_target_name = "your-permission-target-name"
user_name = "desired-username"

# Construct the API endpoint for the permission target
api_endpoint = f"{artifactory_url}/api/security/permissions/{permission_target_name}"

# Construct the payload to add read permission for the given user
payload = {
    "name": "read",
    "includesPattern": "**",
    "repositories": ["your-repo-key"],
    "principals": {
        "users": {
            "user_name": ["read"]
        }
    }
}

headers = {"X-JFrog-Art-Api": api_key}

# Make the API call to set the read permission for the user
response = requests.post(api_endpoint, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print(f"Read permission set for user {user_name} on permission target {permission_target_name}.")
else:
    print(f"Failed to set read permission. Status code: {response.status_code}")
    print(f"Response: {response.text}")
