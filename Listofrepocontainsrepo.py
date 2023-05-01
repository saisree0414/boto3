import requests
import json

# Replace the values below with your Artifactory URL, username, and API key
url = 'https://<your-artifactory-url>/artifactory'
username = '<your-username>'
api_key = '<your-api-key>'

# Replace the value below with the name of your permission target
permission_target = 'example-permission-target'

# Define the API endpoint to retrieve the permission target details
endpoint = f'{url}/api/v2/security/permissions/{permission_target}'

# Define headers with the authentication details
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {username}:{api_key}'
}

# Send a GET request to retrieve the permission target details
response = requests.get(endpoint, headers=headers)

# Parse the JSON response and retrieve the list of repositories associated with the permission target
if response.status_code == 200:
    data = json.loads(response.text)
    repositories = data.get('repositories', [])
    libs_release_repositories = [repo for repo in repositories if 'libs-release' in repo]
    print(f'Repositories associated with the "{permission_target}" permission target that contain "libs-release": {libs_release_repositories}')
else:
    print(f'Error retrieving permission target details: {response.text}')
