import requests
import json

userInput = input("Username: ")

def gitHubFunction(userInput):
    if (isinstance(userInput, str) != True):
        return "The input username is not valid"
    else:
        countRepos = "https://api.github.com/users/" + userInput + "/repos"
        countCommits = "https://api.github.com/users/" + userInput + "/commits"

    return countRepos


print(gitHubFunction(userInput))