import requests
import readtokens
#The three ids needed to generate access token
scope_id=readtokens.scope_id
client_id=readtokens.client_id
client_secret=readtokens.client_secret

#The url that you need to give to the post request
url="https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&client_id="+client_id+"&client_secret="+client_secret+"&redirect_uri=https://creator.zoho.com/appbuilder/quickapps/pedrovelez/form/Clientes/edit&code="+scope_id
response=requests.post(url=url)
print("Code:"+str(response))
print("Content:"+response.content.decode("utf-8"))

    