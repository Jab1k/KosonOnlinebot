import requests
def getid():
    r = requests.get("https://easymobile.uz/getid")
    return r.text