import requests
import json

# Set the Artifactory base URL
base_url = "https://<your-artifactory-domain>/artifactory/api"

# Set your Artifactory credentials
username = "<your-username>"
password = "<your-password>"

# Set the repository key and the user
repository_key = "<repository-key>"
user = "<user>"

# Create the API endpoint URL
endpoint_url = f"{base_url}/security/permissions/{repository_key}"

# Send a GET request to retrieve the permissions of the repository
response = requests.get(endpoint_url, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    permissions = response.json()

    # Find the admin in the list of permissions
    for permission in permissions:
        if user in permission['principals']:
            if permission['admin']:
                admin = permission['principals'][user]
                print(f"The admin of the repository {repository_key} is {admin}")
                break
    else:
        print(f"The user {user} is not found in the permissions of the repository {repository_key}")

else:
    print(f"Failed to retrieve permissions for repository {repository_key}. Error: {response.text}")


#Get Artifactory Repository Admin


#User
#Python script to get the admin of repository in artifactory which user is part of that repository in jfrog artifactory

#To get the admin of a repository in JFrog Artifactory, you can use the JFrog Artifactory REST API. Here's an example Python script that retrieves the admin of a repository given the user who is a part of that repository:
