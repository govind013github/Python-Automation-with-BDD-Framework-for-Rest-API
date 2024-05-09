import requests
from behave import *
from payLoad import *  # import functions from payload file.
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):  # context variables are used to store data that can be shared between different steps in a scenario.
    # Add Book API -
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook  # Note - here getconfig() method is implemented inside configurations.py file and API resources are managed from resources class.
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload("manlkgjklbv", "433")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')           # Parameterization Test Scenarios
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook  # Note - here getconfig() method is implemented inside configurations.py file and API resources are managed from resources class.
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)

####
@given('I have github auth credentials')
def step_impl(context):

    # Authentication example Github
    context.se = requests.session()
    context.se.auth = auth = ('govind013github', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
