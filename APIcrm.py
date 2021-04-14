import requests
import contents
access_token=contents.access_token
print(access_token)
header={'Authorization': 'Zoho-oauthtoken '+access_token}
def get_modules():
    global header
    header={'Authorization': 'Zoho-oauthtoken '+access_token}
    url = "https://www.zohoapis.com/crm/v2/settings/modules"
    response = requests.get(url=url, headers=header)
    print("HTTP Status Code : " + str(response.status_code))
    print(response.content)
    #Create a txt file with the contents
    with open("Responses/getmodule.json","w") as f:
        f.write(response.content.decode("utf-8"))


get_modules()

