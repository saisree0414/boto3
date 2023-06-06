import requests
import json

def get_user_repositories_and_admins(username, artifactory_url, api_key):
    # Set the base URL for the Artifactory REST API
    api_url = f'{artifactory_url}/api'

    # Set the headers for the API request
    headers = {
        'X-JFrog-Art-Api': api_key,
        'Content-Type': 'application/json'
    }

    # Make a GET request to retrieve the user's repositories
    repositories_url = f'{api_url}/security/permissions?users={username}'
    response = requests.get(repositories_url, headers=headers)

    if response.status_code == 200:
        repositories = response.json()
        repo_admins = {}

        # Iterate over the repositories and retrieve the admins for each repository
        for repo in repositories:
            repo_key = repo['repoKey']

            # Make a GET request to retrieve the repository admins
            admins_url = f'{api_url}/security/permissions/{repo_key}'
            admins_response = requests.get(admins_url, headers=headers)

            if admins_response.status_code == 200:
                admins = admins_response.json()['principals']
                repo_admins[repo_key] = admins
            else:
                print(f'Failed to retrieve admins for repository: {repo_key}')

        return repositories, repo_admins
    else:
        print(f'Failed to retrieve repositories for user: {username}')
        return None, None

# Usage example
username = 'exampleuser'
artifactory_url = 'https://your-artifactory-url'
api_key = 'your-artifactory-api-key'

repositories, repo_admins = get_user_repositories_and_admins(username, artifactory_url, api_key)

if repositories and repo_admins:
    print(f'Repositories for user: {username}')
    for repo in repositories:
        repo_key = repo['repoKey']
        print(f'Repository: {repo_key}')

        if repo_key in repo_admins:
            admins = repo_admins[repo_key]
            print('Admins:')
            for admin in admins:
                admin_name = admin['name']
                print(f'- {admin_name}')
        else:
            print('No admins found for this repository')
