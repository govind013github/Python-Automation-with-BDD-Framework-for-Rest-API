import requests
from behave import *
from payLoad import *  # import functions from payload file.
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        context.url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        context.headers = {"Content-Type": "application/json"}
        context.response_deletebook = requests.post(context.url, json=deleteBookPayload(context.bookId), headers=context.headers)

        assert context.response_deletebook.status_code == 200
        res_json = context.response_deletebook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"


