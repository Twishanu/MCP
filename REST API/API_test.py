import requests
import json
def main():
    
    response = requests.get("https://api.github.com/repos/Twishanu/MCP") #HTTPS repo link of this project
    # converting this git into api link "https://github.com/Twishanu/MCP.git" ----> "https://api.github.com/repos/Twishanu/MCP"
    
    # (python dict conversion) the raw json(Response class) format
    data = response.json()
    # print(type(data))
    
    print(json.dumps(data, indent=4)) # .dumps converts the json into string to view the clean form and indent is for indentation
    # print(json.dumps(data))

if __name__ == "__main__":
    main()
    
    
#### We can avoid this testing by using POSTMAN
