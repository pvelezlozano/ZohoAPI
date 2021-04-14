
with open("tokens.txt","r") as tokenfile:
    client_id=tokenfile.readline()
    client_secret=tokenfile.readline()
    scope_id=tokenfile.readline()
    access_token=tokenfile.readline()
