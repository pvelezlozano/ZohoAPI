import requests

#Instrucciones para poder hacer peticiones a la api de creator
#Ir a api-console de Zoho y crear un self client
#Guardar el client id y el client secret
#Elegir el/los scopes que quieres que tengan tus peticiones http
#Cuando eliges los scopes, te daran un codigo
#ESTOS SON LOS SCOPES
#ZohoCreator.form.CREATE,ZohoCreator.report.CREATE,ZohoCreator.report.READ,ZohoCreator.report.UPDATE,ZohoCreator.report.DELETE,ZohoCreator.meta.form.READ,ZohoCreator.meta.application.READ,ZohoCreator.dashboard.READ
#Una vez que tengas el los 3 codigos, has un request de tipo post a zoho, la sintaxis esta abajo
codigo_scope="1000.859ad87b6289d296343b5200fd2c378b.a61c88a11312d060d107cdc152b1adf7"
client_id="1000.QUC7VYEGL2Q1QP03RCXFSSG491FNWB"
client_secret="1055da1930f14ad4ebe6fb70819c69fa299048b42f"
print("Dime lo que quieres hacer: 1. Generar access token\n2. Refrescar access token")
eleccion=input()
if eleccion=="1":
    response=requests.post("https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&client_id="+client_id+"&client_secret="+client_secret+"&redirect_uri=https://creator.zoho.com/appbuilder/quickapps/pedrovelez/form/Clientes/edit&code="+codigo_scope  )
    print("Respuesta:"+str(response))
    print ("Contenido:"+response.content.decode("utf-8"))
    #El access token que te den lo tienes que poner en el archivo de subir.py
elif eleccion=="2":
    #El access token que te dan como respuesta nomas dura una hora, si lo quieres refrescar
    #tienes que hacer un refresh token
    #https://<base_accounts_url>/oauth/v2/token?refresh_token=<refresh_token>&client_id=<client_id>&client_secret=<client_secret>&grant_type=refresh_token
    url_refresh="https://accounts.zoho.com/oauth/v2/token?refresh_token="+codigo_scope+"&client_id="+client_id+"&client_secret="+client_secret+"&grant_type=refresh_token"
    refrescar=requests.post(url=url_refresh)
    print(refrescar,refrescar.content)