import json

json_input = '''
{
  "tokens": [
    {
      "token_id": "123",
      "issuer": "jf-artifactory@123123",
      "subject": "jf-artifactory@123123/users/theusername",
      "expiry": 145154545,
      "refreshable": true,
      "issued_at": 144152345
    }
  ]
}
'''

# Parse the JSON input
data = json.loads(json_input)

# Extract the username from the subject field
subject = data['tokens'][0]['subject']
username = subject.split('/users/')[1]

print(f"Username: {username}")


#In this script, the provided JSON input is stored in the json_input variable. The json.loads() function is used to parse the JSON data into a Python dictionary. Then, the username is extracted by splitting the "subject" field using the "/users/" delimiter.

#The script assumes that the JSON input contains only one token. If there are multiple tokens in the "tokens" list, you can modify the code to iterate over the list and extract usernames accordingly.
