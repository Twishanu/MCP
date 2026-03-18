import requests
import os
from dotenv import load_dotenv

load_dotenv()
def main():
    url = "https://api.github.com/repos/Twishanu/Repo-made-with-POST-notPvt"
    TOKEN = os.getenv("github_pat_token")
    if not TOKEN:
        print("pat token not found")
        return
    data = {
        "description" : "For testing it with Python"
    }
    headers = {
        "Authorization" : f"Bearer {TOKEN}",
        "User-Agent": "PythonApp"
    }
    
    response = requests.patch(url, json = data, headers=headers)
    if response.status_code == 200:
        print(response.json()) #converting the response into <'dict'>
    else:
        print(f"Error: {response.status_code}, {response.text}")
if __name__ == "__main__":
    main()