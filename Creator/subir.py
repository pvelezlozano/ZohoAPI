import requests
import json
#Aqui en este programa se haran las peticiones para crear, obtener y modificar los reportes de nuestra app
#OJO, EL PARAMETRO DATA EN POST,GET Y PATCH SE DEBE PASAR COMO STRING
access_token="1000.876cf9472b7827e119ffb697f5ee79c1.7e92b65e1d9824d43b3d8f95c605661c"
header={"Authorization": "Zoho-oauthtoken "+access_token}
username="quickapps"
app_name="pedrovelez"
nombre_reporte="All_Pythons"
nombre_form="Python"
print("1. Get records by id")
print("2. Get records")
print("3. Update records by id")
print("4. Update records")
print("5. Crear records")
eleccion=int(input("Dame un numero para hacer tu eleccion\n"))
#Get records, detail view (gets records per id)
if (eleccion==1):
    id_record="3461648000019089188"
    
    r1=requests.get("https://creator.zoho.com/api/v2/"+username+"/"+app_name+"/report/"+nombre_reporte+"/"+id_record,headers=header)
    contenido=r1.content.decode("utf-8")
    print(contenido)
#Get records, quick view (gets all records) ?from=50&limit=100 MAX 200
elif eleccion==2:
    r2=requests.get("https://creator.zoho.com/api/v2/"+username+"/"+app_name+"/report/"+nombre_reporte,headers=header)
    todos_los_records=r2.content.decode("utf-8")
    print(todos_los_records)
#Update Record by ID
elif eleccion==3:
    url="https://creator.zoho.com/api/v2/"+username+"/"+app_name+"/report/"+nombre_reporte+"/"+"3461648000019107005"
    data={
        "data":{
            "Nombre":{
                "prefix":"",
                "first_name":"Hector Manuel",
                "last_name":"Gonzalez Dib",
                "suffix": ""
            },
            "Edad":28
        },
        "result":{
            "fields":["Nombre", "Edad"],
            "message":True,
            "tasks":True
        }
    }
    r3=requests.patch(url=url,headers=header,data=str(data))
    print(r3,r3.content)
#Update Record
elif eleccion==4:
    pass
#Crear Record usando post
elif eleccion==5:
    url="https://creator.zoho.com/api/v2/"+username+"/"+app_name+"/form/"+nombre_form
    data={
        "data":{
            "Nombre":{
                "prefix":"",
                "first_name":"Pedro ",
                "last_name":"Velez",
                "suffix": ""
            },
            "Edad":20
        },
        "result":{
            "fields":["Nombre", "Edad"],
            "message":True,
            "tasks":True
        }
    }
    r5=requests.post(url=url,headers=header,data=str(data))
    print(r5,r5.content)

    
