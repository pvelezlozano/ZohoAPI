import requests
import readstuff
#El access token que te dan como respuesta nomas dura una hora, si lo quieres refrescar
#tienes que hacer un refresh token
#https://<base_accounts_url>/oauth/v2/token?refresh_token=<refresh_token>&client_id=<client_id>&client_secret=<client_secret>&grant_type=refresh_token

codigo_scope=readstuff.scope_id
client_id=readstuff.client_id
client_secret=readstuff.client_secret
url_refresh="https://accounts.zoho.com/oauth/v2/token?refresh_token="+codigo_scope+"&client_id="+client_id+"&client_secret="+client_secret+"&grant_type=refresh_token"
refrescar=requests.post(url=url_refresh)
print(refrescar,refrescar.content)