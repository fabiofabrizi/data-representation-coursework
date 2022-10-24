"""
    This is Assignment 4 - Download a file from Github, replace with my own name (Fabio)
    and upload again to github.

    Import necessary libraries:
    - gitconfig: private token used for Github authentication
    - credentials: The user and desired repo
    - base64: For file encoding on upload

    Design Decisions

    There's 3 files to do this:
    1) assignment-04-github.py (this file)
    2) credentials.py - user credentials of github username and repo we're working with
    3) gitconfig.py - where the github token is stored

    Please note: 'testing2.txt' is the file that contains 'Andrew'.
    'result.txt' is the file that's uploaded back up.
    NB: The private key has NOT been uploaded to github, 
    but test this by downloading, changing the config to match your 
    username and repo and creating a reference to your own key.

"""

# to use this install package
from github import Github
import requests
# Import key
from gitconfig import config as cfg
import base64
# Import the user and desired repo
from credentials import githubuser as gu, githubrepo as gr

# Call the github private key
apikey = cfg["githubkey"]
# Reference key with Github library
g = Github(apikey)

# Call user credentials from file
user = gu["user"]
priv_repo = gr["repo"]

# Specify file with text to replace
desired_file = "testing2.txt"

# Get the repo and the contents of the file
repo = g.get_repo(f'{user}/{priv_repo}')
fileInfo = repo.get_contents("testing2.txt")

# After that, get the download url - this is a key value pair, 
# check the associated lab to see JSON outpu
urlOfFile = fileInfo.download_url

# Get the information from the download page
response = requests.get(urlOfFile)

# Text from the response is the content of the file
contentOfFile = response.text

# File replacement - check with Andrew if he's happy 
# with 2 files, otherwise overwrite the same file.
with  open("Saved_File.txt", "w") as fp:
    fp.writelines(contentOfFile)

f1 = open('Saved_File.txt', 'r')
f2 = open('result.txt', 'w')

for line in f1:
    f2.write(line.replace('Andrew', 'Fabio'))
f1.close()
f2.close()

# Assign to another variable
data = open("result.txt", "r").read()

r = requests.put(
    f'https://api.github.com/repos/fabiofabrizi/aprivateone/contents/result.txt',
    headers = {
        'Authorization': f'Token {apikey}'
    },
    json = {
        "message": "add a new file via python script",
        "content": base64.b64encode(data.encode()).decode()
    }
)
# Check status code to see if it worked
print(r.status_code)
