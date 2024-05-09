import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName': 'Govind'}, )
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))                        # Here python smartly converts dic to list looking at response.
# print(dict_response[0]['isbn'])                   # so inside List at 0th index we have dic key-value isbn.


json_response = response.json()                # To avoid above confusion on return type and skip json.loads method we can use this.
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200             # To check response code and assert
print(response.headers)                        # To check headers
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'      # To perform headers assertion
print(response.cookies)                        # To check cookies

# Retrieve the book details with ISBN value 'bcg'
for actualbook in json_response:
    print(type(actualbook))
    if actualbook['isbn'] == 'bcg':
        print(actualbook)
        break

expectedBook = {
        "book_name": "selenium with java",
        "isbn": "bcg",
        "aisle": "228"
    }

assert actualbook == expectedBook






