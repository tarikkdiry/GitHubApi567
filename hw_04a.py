import requests
import json
from sys import getsizeof
import pprint

userInput = input("Username: ")

def gitHubFunction(userInput):
    if (isinstance(userInput, str) != True):
        return "The input username is not valid"

    repoName = requests.get("https://api.github.com/users/" + userInput + "/repos")
    data = repoName.json()
    
    for i in data:
        name = i["name"]
        print(name)


# def gitHubFunction(userInput):
#     if (isinstance(userInput, str) != True):
#         return "The input username is not valid"    

#     result = str("https://api.github.com/users/" + userInput + "/repoName")
#     parsed_result = json.dumps(result)

#     return parsed_result


# print(gitHubFunction(userInput))
print(gitHubFunction(userInput))