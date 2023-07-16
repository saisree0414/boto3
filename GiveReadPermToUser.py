import requests
import json

# Artifactory API endpoint
api_url = "https://your-artifactory-instance/api/security/permissions"

# Artifactory credentials
username = "your-username"
password = "your-password"

# Repository permission target details
repo_permission_target = "your-permission-target-name"
repo_name = "your-repository-name"
username_to_grant = "username-to-grant"

# Create a session
session = requests.Session()
session.auth = (username, password)

# Retrieve the existing permissions
response = session.get(api_url)
response.raise_for_status()
permissions = response.json()

# Find the target permission
target_permission = None
for permission in permissions:
    if permission["name"] == repo_permission_target:
        target_permission = permission
        break

# If the permission target is not found, exit the script
if not target_permission:
    print(f"Permission target '{repo_permission_target}' not found.")
    exit()

# Add the read permission to the user
permissions_to_add = [
    {"name": "read", "repo": repo_name, "includesPattern": "**", "excludesPattern": ""},
]

# Update the permission target with the new permissions
target_permission["includesPattern"] += permissions_to_add

# Update the permission target in Artifactory
response = session.put(f"{api_url}/{target_permission['name']}",
                       headers={"Content-Type": "application/json"},
                       data=json.dumps(target_permission))
response.raise_for_status()

# Grant access to the user
response = session.put(f"{api_url}/{target_permission['name']}/users/{username_to_grant}")
response.raise_for_status()

# Print the success message
print(f"Read access granted to user '{username_to_grant}' for permission target '{repo_permission_target}' in repository '{repo_name}'.")
