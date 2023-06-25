import requests

def get_permission_target(username):
    # Replace 'YOUR_JFROG_URL' with the actual URL of your JFrog platform instance
    url = f'YOUR_JFROG_URL/api/v1/security/permissions/{username}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_TOKEN'  # Replace 'YOUR_API_TOKEN' with your actual API token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        permission_target = data['permissionTarget']
        admin = data['admin']
        return permission_target, admin
    else:
        return None, None

def write_permission_targets(username_list, output_file):
    with open(output_file, 'w') as file:
        for username in username_list:
            permission_target, admin = get_permission_target(username.strip())
            if permission_target is not None:
                file.write(f'Username: {username.strip()}\n')
                file.write(f'Permission Target: {permission_target}\n')
                file.write(f'Admin: {admin}\n')
                file.write('\n')

# Read the list of usernames from a file
with open('username_list.txt', 'r') as username_file:
    usernames = username_file.readlines()

# Specify the output file path
output_file_path = 'output.txt'

# Write permission targets and admin to the output file
write_permission_targets(usernames, output_file_path)

print('Permission targets and admin have been written to the output file.')

#Save the script to a Python file (e.g., permission_targets.py), and place the list of usernames in a separate file (e.g., username_list.txt). Then, when you run the script, it will fetch the permission target and admin for each username in the list and write the information to an output file (e.g., output.txt).
#
