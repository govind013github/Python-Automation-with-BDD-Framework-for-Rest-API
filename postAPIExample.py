import requests
import configparser
from payLoad import *  # import functions from payload file.
from utilities.configurations import *
from utilities.resources import *

# Add Book API -
url = getConfig()['API'][
          'endpoint'] + ApiResources.addBook  # Note - here getconfig() method is implemented inside configurations.py file and API resources are managed from resources class.
headers = {"Content-Type": "application/json"}
query = 'SELECT * FROM apidevelop.books'
addBook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers)
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)

# Delete Book API -
url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers = {"Content-Type": "application/json"}
response_deletebook = requests.post(url, json=deleteBookPayload(bookId), headers=headers)

assert response_deletebook.status_code == 200
res_json = response_deletebook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication example Github
se = requests.session()
se.auth = auth = ('govind013github', getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url, verify=False, auth=('govind013github', getPassword()))

print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)




