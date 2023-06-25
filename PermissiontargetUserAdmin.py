import requests

# JFrog Platform details
base_url = "https://your-jfrog-instance-url/api/v2"
api_key = "your-api-key"

# Function to retrieve permission targets
def get_permission_targets():
    url = f"{base_url}/security/permissions"
    headers = {
        "Content-Type": "application/json",
        "X-JFrog-Art-Api": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve permission targets.")
        return None

# Function to print permission target, user, and admin
def print_permission_target(permission_target, username):
    permission_name = permission_target['name']
    for user in permission_target['users']:
        if user['name'] == username:
            print("Permission Target:", permission_name)
            print("User:", user['name'])
            print("Admin:", user['admin'])

# Main function
def main():
    username = input("Enter the username: ")
    permission_targets = get_permission_targets()
    if permission_targets is not None:
        for target in permission_targets:
            print_permission_target(target, username)

# Run the script
if __name__ == "__main__":
    main()
#When you run the script, it will prompt you to enter the username for which you want to retrieve the permission target, user, and admin information. It will then fetch the permission targets from the JFrog Platform using the provided API key and display the relevant information for the specified username.
#Please note that this script assumes you have the necessary permissions and API access to retrieve the permission targets from the JFrog Platform.
