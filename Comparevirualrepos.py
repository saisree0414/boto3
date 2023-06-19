import requests

def get_virtual_repos(base_url, username, password):
    url = base_url + '/artifactory/api/repositories?type=virtual'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        repos_data = response.json()
        return repos_data['results']
    else:
        print('Failed to retrieve virtual repositories.')
        return []

def compare_virtual_repos(base_url1, base_url2, username1, password1, username2, password2):
    repos1 = get_virtual_repos(base_url1, username1, password1)
    repos2 = get_virtual_repos(base_url2, username2, password2)

    for repo1 in repos1:
        for repo2 in repos2:
            if repo1['key'] == repo2['key']:
                if set(repo1['repositories']) != set(repo2['repositories']):
                    print(f"Virtual Repository '{repo1['key']}' has different associated repositories.")
                break

# Replace with your Artifactory base URLs, usernames, and passwords
base_url1 = 'http://artifactory1.example.com'
base_url2 = 'http://artifactory2.example.com'
username1 = 'your_username1'
password1 = 'your_password1'
username2 = 'your_username2'
password2 = 'your_password2'

compare_virtual_repos(base_url1, base_url2, username1, password1, username2, password2)
