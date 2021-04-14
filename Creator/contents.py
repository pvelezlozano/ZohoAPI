
with open("Information/tokens.txt","r") as tokenfile:
    client_id=tokenfile.readline().strip("\n")
    client_secret=tokenfile.readline().strip("\n")
    scope_id=tokenfile.readline().strip("\n")
    access_token=tokenfile.readline().strip("\n")

with open("Information/appmeta.txt","r") as appfile:
    username=appfile.readline().strip("\n")
    app_name=appfile.readline().strip("\n")
    report_name=appfile.readline().strip("\n")
    form_name=appfile.readline().strip("\n")

