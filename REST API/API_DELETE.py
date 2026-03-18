import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
def main():
    TOKEN = os.getenv("github_pat_token")
    URL = "https://api.github.com/repos/Twishanu/Repo-made-with-POST-notPvt"
    if not TOKEN:
        print("Token not found in env")
        return
    headers = {
        "Authorization" : f"Bearer {TOKEN}"
    }
    response = requests.delete(URL, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error :{response.status_code}, {response.text}")
if __name__ == "__main__":
    main()