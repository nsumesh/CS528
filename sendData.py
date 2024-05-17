import requests
import json

url = 'http://172.31.163.225:8000/receive_data'  

json_files = ['X1.json', 'Y1.json', 'X2.json', 'Y2.json', 'Confidence.json']

def send_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        response = requests.post(url, json=data)
        print(f"Sent {file_name}: {response.status_code}, {response.text}")

for file in json_files:
    send_json(file)
