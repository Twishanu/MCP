import requests
import os
from dotenv import load_dotenv

load_dotenv()
## adding a new repo in my github using HTTPS POST
def main():
    url = "https://api.github.com/user/repos"  #### the link where I would create a new repo
    github_pat_token = os.getenv("github_pat_token")
    data = {
        "name" : "Repo-made-with-POST-notPvt",
        # "private" : True
    }
    ### Now the reverse, this python object "data" needs to be in the form of JSON to POST in Github
    headers = {
        "Authorization" : f"token {github_pat_token}"
    }
    response = requests.post(url, json=data, headers=headers)
    print(type(response),"\n")  ## <class 'requests.models.Response'> || difficult to read
    print(response.json(),"\n")
    print(type(response.json())) ## dict
if __name__ == "__main__":
    main()