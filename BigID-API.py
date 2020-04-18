import requests
from pprint import pprint
import json

def sessionsBidID():
    url = "https://23.97.206.170/api/v1/sessions"
    payload = "{\"username\":\"paul@starrettconsultinginc.com\",\"password\":\"Starret12\"}"
    headers = {
             'accept': 'application/json',
             'content-type': 'application/json'
        }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.status_code)
    print(headers)
    # response.json() returns a dict.
    response_dict = response.json()
    pprint(response_dict)

    # turns JSON, a dict in Python, into a string.
    response_dict = json.dumps(response_dict)
    print(response_dict)

    # write JSON to a file.
    with open('data.txt', 'w') as outfile:
        json.dump(response_dict, outfile)

    # read JSON from a file and return a dict.
    with open('data.txt') as json_file:
        data = json.load(json_file)

    # turn json.load string into z dict with json.loads
    json_dict = json.loads(data)
    print(json_dict)
    auth_token = json_dict['auth_token']
    print(auth_token)

    #save auth token to file for later use
    with open('auth.txt', 'w') as outfile:
        outfile.write(auth_token)

def dataCatalogBidID():
    url = "https://23.97.206.170/api/v1/data-catalog"

    # read JSON from a file and return a dict.
    with open('auth.txt') as infile:
        auth_data = infile.read()
    print(auth_data)

    querystring = {"format": "json"}
    headers = {
             #'accept': 'application/json',
             'content-type': 'application/json',
             'authorization': auth_data
        }

    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    print(response.status_code)
    print(headers)
    # response.json() returns a dict.
    response_dict = response.json()
    pprint(response_dict)

    # turns JSON, a dict in Python, into a string.
    response_dict = json.dumps(response_dict)
    print(response_dict)

    # write JSON to a file.
    with open('data_catalog.txt', 'w') as outfile:
        json.dump(response_dict, outfile)

    # NOTE THAT THIS CALL IS NOT NECESSARY IN PRODUCION. read JSON from a file and return a dict.
    with open('data_catalog.txt') as json_file:
        data = json.load(json_file)

#sessionsBidID()

dataCatalogBidID()



