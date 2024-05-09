import json

# ***** Parse content present in JSON String below :
courses = '{"name": "GovindSurya","languages" :["Java","Python"]}'     # Here we take 'JSON body' in String variable.

# Json Loads method' parses json string and it returns dictionary.
dict_courses = json.loads(courses)                  # here we assigned 'json-body data' to a dict variable.
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# Q.To get the first language taught by trainer in above courses.
print(dict_courses['languages'])
# list_language = dict_courses['languages']         # here we assigned 'dict data' to a list variable by checking type.
# print(type(list_language))
# print(list_language[0])                         # 1st approach prints - java

# Use below alternative way -
print(dict_courses['languages'][0])               # 2nd approach prints - java

# **** Parse content present in JSON File (JsonParsingdata.txt) :

with open('JsonParsingdata.txt') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['address'][1]['country'])
    print(data['bankdetails']['website'])
    print(type(data['bankdetails']))
# Q. Get street location from Country 'USA'
    print(type(data['address']))
    for addr in data['address']:
       # print(addr)
        if addr['country'] == 'USA':
            print(addr['street'])
            assert addr['street'] == 'statue of liberty'

# To compare two JSON Schemas using Python Dictionaries.
with open('JsonParsingdata2.txt') as fi:
    data2 = json.load(fi)
    assert (data == data2)                                # Assert and compare two JSON Schemas




