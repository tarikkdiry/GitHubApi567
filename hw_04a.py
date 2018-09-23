import requests
import json
from sys import getsizeof
import pprint

userInput = input("Username: ")

def gitHubFunction(userInput):
    if (isinstance(userInput, str) != True):
        return "The input username is not valid"
    elif((requests.get("https://api.github.com/users/" + userInput + "/repos")).json() == []):
        return "This account does not have any repositories"
    else:
        repoName = requests.get("https://api.github.com/users/" + userInput + "/repos")
        data = repoName.json()
        
        for i in data:
            name = i["name"]
            commits = requests.get("https://api.github.com/users/" + userInput + "/" + name + "/commits")
            commits_data = len(commits.json())
            # print("Repo:" + name + "Number of commits: " + )
            print("Repo:" + name + "Number of commits: " + str(commits_data))


print(gitHubFunction(userInput))