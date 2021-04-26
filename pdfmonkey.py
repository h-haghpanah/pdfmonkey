import requests
from requests.structures import CaseInsensitiveDict
import json
from time import sleep

def pdfmonkey(secret,document_template_id,payload):

    url = "https://api.pdfmonkey.io/api/v1/documents"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = secret
    headers["Content-Type"] = "application/json"

    # If you need read payload from file
    # f = open("payload.txt", "r")
    # payload = f.read()

    data = r'{"document": {"document_template_id": "' + document_template_id + r'","payload": ' + payload + r',"status": "pending"}}' #create payload data
    resp = requests.post(url, headers=headers, data=data)
    document_id = json.loads(resp.text)["document"]["id"]
    sleep(3)
    url = "https://api.pdfmonkey.io/api/v1/documents/"+document_id
    resp = requests.get(url, headers=headers)
    download_url = json.loads(resp.text)["document"]["download_url"]
    retry_count = 0
    while True: #try get pdf url if still not generated
        if retry_count < 10:
            if download_url == None:
                sleep(3)
                resp = requests.get(url, headers=headers)
                download_url = json.loads(resp.text)["document"]["download_url"]
                retry_count += 1
            else:
                break
        else:
            print("Generating PDF Failed From PDF Monkey !")
            break
    return download_url

