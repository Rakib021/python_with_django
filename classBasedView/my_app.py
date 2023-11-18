import requests
import json

URL ="http://127.0.0.1:8000/studentapi/"

def getData(id= None):
    data ={}
    if id is not None:
        data ={'id':id}

    json_data = json.dumps(data)

    res = requests.get(url =URL,data =json_data)
    data = res.json()
    print(data)
getData(2)

def postData():
    data ={
        'name':'ravi',
        'roll': 103,
        'city':'chittagong'
    }
    json_data = json.dumps(data)
    res = requests.post(url =URL,data =json_data)
    
    data = res.json()
    print(data)
# postData()
def updateData():
    data ={
        'id':5,
        'name':'safi',

        'city':'chittagong'
    }
    json_data = json.dumps(data)
    res = requests.put(url =URL,data =json_data)
    
    data = res.json()
    print(data)
# updateData()  

def deleteData():
    data ={
        'id':5,
        
    }
    json_data = json.dumps(data)
    res = requests.delete(url =URL,data =json_data)
    
    data = res.json()
    print(data)
# deleteData()   

