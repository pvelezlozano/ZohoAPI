import requests
import json
import contents

#The three ids needed to generate access token
scope_id=contents.scope_id
client_id=contents.client_id
client_secret=contents.client_secret

#The url that you need to give to the post request
redi_uri="https://crm.zoho.com/"
url="https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&client_id="+client_id+"&client_secret="+client_secret+"&redirect_uri="+redi_uri+"&code="+scope_id
response=requests.post(url=url)
print("Code:"+str(response))
print("Content:"+response.content.decode("utf-8"))