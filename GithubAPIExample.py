import requests
import configparser
from payLoad import *  # import functions from payload file.
from utilities.configurations import *
from utilities.resources import *


# Authentication example Github

def login_to_github_with_token(token):
    # Construct the request headers with the provided headers
    headers = {
        'Authorization': f'Bearer {token}',  # Include your access token for authentication
        'Accept': 'application/vnd.github.v3+json',  # Specify the API version
        'X-GitHub-Api-Version': '2022-11-28'  # Specify the GitHub API version
    }

    # Make a GET request to verify login status
    response = requests.get('https://api.github.com/user', headers=headers)

    # Check the response status code
    if response.status_code == 200:
        user_info = response.json()
        print(f"Logged in as: {user_info['login']}")
    else:
        print(f"Failed to log in. Status code: {response.status_code}")
        print(response.text)

    url2 = "https://api.github.com/user/repos"
    response = requests.get(url2, headers=headers)
    print(response.status_code)
    print(response.text)

# Replace 'TOKEN' with your actual GitHub access token
token = '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'

login_to_github_with_token(token)

# url2 = "https://api.github.com/user/repos"
# response = requests.get(url2, headers=headers)
# print(response.status_code)



