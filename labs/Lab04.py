"""
    Topic 05 Assignment on pulling info from a private repo on Github, and updating that repo

    Import necessary libraries:
    - requests for HTTP requests
    - json for working with JSON
    - pprint (pretty print) to format JSON that's printed to screen
    - gitconfig: private token used for Github authentication
    - credentials: The user and desired repo

    Design Decisions

    There's 3 files to do this:
    1) assignment-04-github.py (this file)
    2) credentials.py - user credentials of github username and repo we're working with
    3) gitconfig.py - where the github token is stored

    How it works
    
    The user and repo are read in from the file and form part of the url that we're working with.
    The api key (token) is referenced and we use the requests library to get information about the repo, 
    download it into a JSON file.
    Using the key-value pairs from the JSON file we output some details about the repo.

    We then use requests again (requests.put) to put the JSON file back into the repo, 
    with a message.
    NB - it doesn't have to be the JSON file that was saved, it can be another one, 
    the decision was just made to use it because it was lying around.

"""
import requests
import json
from pprint import pprint
import base64
from gitconfig import config as cfg
from credentials import githubuser as gu, githubrepo as gr

# Call user credentials from file
user = gu["user"]
priv_repo = gr["repo"]

# private repo url with credentials (user, repo)
url = f"https://api.github.com/repos/{user}/{priv_repo}"

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

# Call the token from the configuration file
# and embed into the response
apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

# output the response to the screen to see if it worked
print (response.status_code)
#print (response.json())

# Specify filename, open it and dump JSON response in it
filename = "repos-private.json"
with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
    # Check output with pprint
    #pprint(repoJSON)

# Read the JSON response that was assigned to repoJSON 
# Print repo details to the screen:
    owner = repoJSON["owner"]["login"]
    description = repoJSON["description"]
    creation_date = repoJSON["created_at"]
    watcher_num = repoJSON["watchers"]
    print(f"The owner of the repo is: {owner}")
    print(f"The description is: {description}")
    print(f"The repo was created at: {creation_date}")
    print(f"The number of watchers are: {watcher_num}")


# Now, upload the JSON file to Github using requests.put
# 
#repo = 'fabiofabrizi/aprivateone'
#repo = f"{user}/{priv_repo}"
data = open(filename, "r").read()

r = requests.put(
    f'https://api.github.com/repos/{user}/{priv_repo}/contents/{filename}',
    headers = {
        'Authorization': f'Token {apikey}'
    },
    json = {
        "message": "add a new file via python script",
        "content": base64.b64encode(data.encode()).decode()
    }
)
print(r.status_code)

# Test what the output is
#pprint(r.json())
