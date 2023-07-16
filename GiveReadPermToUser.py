from jfrog import Artifactory

# Artifactory credentials
url = "https://your-artifactory-instance"
username = "your-username"
password = "your-password"

# Permission target and user details
permission_target_name = "your-permission-target-name"
username_to_grant = "username-to-grant"

# Create an Artifactory instance
artifactory = Artifactory(url, username, password)

# Get the permission target
permission_target = artifactory.security.get_permission_target(permission_target_name)
if not permission_target:
    print(f"Permission target '{permission_target_name}' not found.")
    exit()

# Get the existing users with permissions
users = permission_target.get("users", [])

# Check if the user permission already exists
for user_permission in users:
    if user_permission["name"] == username_to_grant:
        # Add read permission to the existing user permission
        if "r" not in user_permission["scopes"]:
            user_permission["scopes"].append("r")
        break
else:
    # Create a new user permission with read access
    user_permission = {
        "name": username_to_grant,
        "scopes": ["r"]
    }
    users.append(user_permission)

# Update the permission target with the modified user permissions
permission_target["users"] = users
artifactory.security.update_permission_target(permission_target)

# Print the success message
print(f"Read access granted to user '{username_to_grant}' for permission target '{permission_target_name}'.")
