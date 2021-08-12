import json
import requests

def read_file_data():
    #how to read froma json file
    f = open('./data.json','r') 
    json_obj = json.load(f)
    print(json_obj)

def read_api_data():
    #how to read from a api
    endpoint = "https://python-syllabus.herokuapp.com/beginners"
    r = requests.get(endpoint)
    if r.status_code == 200:
        print("connection established")
        #Now it will return the data 
        json_data = r.json()
        #converts the json data into a string
        data = json.dumps(json_data,indent=4)
        with open("save.json","w") as outfile:
            outfile.write(data)
    else:
        print("connection cannot be found")
    return json_data

def read_each_item_in_json_data():
    with open("save.json","r") as f:
        data = json.load(f)
        print(data)
        for i in data:
            print(i["name"][5])

read_each_item_in_json_data()
# read_api_data()