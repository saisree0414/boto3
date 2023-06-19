import requests

# JFrog platform API endpoints
platform1_url = 'https://platform1.example.com/api/v1'
platform2_url = 'https://platform2.example.com/api/v1'

# JFrog platform API credentials
username = 'your_username'
password = 'your_password'

# Virtual repository name
virtual_repo = 'your_virtual_repo_name'

# Output file name
output_file = 'repo_comparison.txt'

def get_associated_repos(api_url):
    url = f'{api_url}/repositories?type=virtual&repos={virtual_repo}'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    repositories = response.json()[0]['repositories']
    return set(repositories)

def compare_associated_repos():
    platform1_repos = get_associated_repos(platform1_url)
    platform2_repos = get_associated_repos(platform2_url)

    if platform1_repos != platform2_repos:
        with open(output_file, 'w') as file:
            file.write(f"Virtual Repository: {virtual_repo}\n")
            file.write("Associated Repositories in Platform 1:\n")
            file.write('\n'.join(platform1_repos))
            file.write("\n\nAssociated Repositories in Platform 2:\n")
            file.write('\n'.join(platform2_repos))
        print(f"Comparison result written to '{output_file}'")
    else:
        print(f"Associated repositories in '{virtual_repo}' are the same between the platforms.")

compare_associated_repos()
