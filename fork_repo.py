'''
This program is used to fork all public repositories from a user profile given a username.

Instructions:
Step 1: Install the library github3.py by entering the command '$ pip install github3.py'
Step 2: Provide login details of your account by providing your username and password or personal access token
Step 3: Run the program with 'python3 fork_repo.py'
Step 4: Provide the username of the account that you are forking repositories from 
'''

# importing necessary libraries
import git
import os
import github3
from github3 import login

# Creating input argument for username of interest
given_user = input('Enter GitHub username: ')

# LOG IN AND AUTHENTICATION 

# Method 1: using username and password
#github = github3.login(username=username, password=password)

# Method 2: using a token
github = github3.login(token='token')

# printing all public repositories for given user
for repository in github.repositories_by(given_user):
    print('{0}'.format(repository))

# forking all public repositories for given user
for repository in github.repositories_by(given_user):
    repository.create_fork()

# if you want to fork an organization you can do the following:
# for repository in github.repositories_by(user):
#     repository.create_fork(oranization)
