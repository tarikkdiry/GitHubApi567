import requests
import json
from sys import getsizeof
import pprint
import os

userInput = input("Username: ")

def gitHubFunction(userInput):
    if (isinstance(userInput, str) != True):
        return "The input username is not valid"
    elif((requests.get("https://api.github.com/users/" + userInput + "/repos")).json() == []):
        return "This account does not have any repositories"
    else:
        repoName = requests.get("https://api.github.com/users/" + userInput + "/repos")
        data = repoName.json()
        # print(data)
        try:
            for i in data:
                name = i["name"]
                commits = requests.get("https://api.github.com/users/" + userInput + "/" + name + "/commits")
                # commits_data = len(commits.json())
                commits_data = commits.json()
                print("Repo:" + name + " Number of commits: " + str(commits_data))
        except:
            print("================================================================")
            print("     YOU HAVE EXCEEDED YOUR API RATE LIMIT. SEE BELOW")
            print("================================================================")
            print(os.system("curl -i https://api.github.com/users/" + userInput))



print(gitHubFunction(userInput))