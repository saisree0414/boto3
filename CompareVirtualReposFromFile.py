import requests

def compare_virtual_repos(virtual_repos, platform1_url, platform2_url, output_file):
    for repo in virtual_repos:
        repo_url1 = platform1_url + '/api/repositories/' + repo
        repo_url2 = platform2_url + '/api/repositories/' + repo

        response1 = requests.get(repo_url1)
        response2 = requests.get(repo_url2)

        if response1.status_code == 200 and response2.status_code == 200:
            data1 = response1.json()
            data2 = response2.json()

            if data1['repositories'] != data2['repositories']:
                with open(output_file, 'a') as file:
                    file.write(repo + '\n')
        else:
            print(f"Error retrieving repository information for {repo}")

# Read virtual repositories from a file (one repository per line)
virtual_repos_file = 'virtual_repos.txt'
with open(virtual_repos_file, 'r') as file:
    virtual_repos = [line.strip() for line in file]

# JFrog platform URLs
platform1_url = 'https://platform1.jfrog.io'
platform2_url = 'https://platform2.jfrog.io'

# Output file to write the different virtual repositories
output_file = 'different_virtual_repos.txt'

# Compare virtual repositories
compare_virtual_repos(virtual_repos, platform1_url, platform2_url, output_file)

Compare JFrog Virtual Repos


User
Python script to write a virtual repos into file if associated repos in virtual repo is not same in two jfrog platforms. Input is virtual repos list from file.

ChatGPT
Sure! I can help you with that. Here's a Python script that reads a list of virtual repositories from a file and checks if the associated repositories in two JFrog platforms are the same. If they are different, it writes the virtual repository to a file.

python
Copy code
import requests

def compare_virtual_repos(virtual_repos, platform1_url, platform2_url, output_file):
    for repo in virtual_repos:
        repo_url1 = platform1_url + '/api/repositories/' + repo
        repo_url2 = platform2_url + '/api/repositories/' + repo

        response1 = requests.get(repo_url1)
        response2 = requests.get(repo_url2)

        if response1.status_code == 200 and response2.status_code == 200:
            data1 = response1.json()
            data2 = response2.json()

            if data1['repositories'] != data2['repositories']:
                with open(output_file, 'a') as file:
                    file.write(repo + '\n')
        else:
            print(f"Error retrieving repository information for {repo}")

# Read virtual repositories from a file (one repository per line)
virtual_repos_file = 'virtual_repos.txt'
with open(virtual_repos_file, 'r') as file:
    virtual_repos = [line.strip() for line in file]

# JFrog platform URLs
platform1_url = 'https://platform1.jfrog.io'
platform2_url = 'https://platform2.jfrog.io'

# Output file to write the different virtual repositories
output_file = 'different_virtual_repos.txt'

# Compare virtual repositories
compare_virtual_repos(virtual_repos, platform1_url, platform2_url, output_file)
To use this script, you need to make sure you have the requests library installed. You can install it by running pip install requests in your terminal.

#Please replace 'https://platform1.jfrog.io' and 'https://platform2.jfrog.io' with the URLs of your two JFrog platforms. Also, make sure to provide the correct path to the virtual_repos.txt file and specify the desired output file name in the output_file variable.

#The script reads the virtual repositories from the virtual_repos.txt file, one repository per line. It then compares the associated repositories of each virtual repository in the two JFrog platforms. If the associated repositories are different, the virtual repository is written to the different_virtual_repos.txt file.
