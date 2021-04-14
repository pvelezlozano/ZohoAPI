import requests
import json
import contents
def menu():
    print("1. Get records by id")
    print("2. Get records")
    print("3. Update records by id")
    print("4. Update records")
    print("5. Crear records")
    eleccion=int(input("Dame un numero para hacer tu eleccion\n"))
    return eleccion


#This script is where we will make petitions to create, get and change records of our Creator App
#NOTEE, the paremeter data in post, update,get and patch must be given as a string, otherwise an error will be shown


access_token=contents.access_token
header={"Authorization": "Zoho-oauthtoken "+access_token}
username=contents.username
app_name=contents.app_name
nombre_reporte=contents.report_name
nombre_form=contents.form_name

eleccion=menu()

#Get records, detail view (gets records per id)
if (eleccion==1):
    id_record="3461648000019089188"
    url="https://creator.zoho.com/api/v2/"+username+"/"+app_name+"/report/"+nombre_reporte+"/"+id_record
    print(url)
    r1=requests.get(url=url,headers=header)
    contenido=r1.content.decode("utf-8")
    contenidojson=json.loads(contenido)
    print(contenidojson)
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

    
