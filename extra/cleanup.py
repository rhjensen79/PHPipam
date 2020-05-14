#PHPipam Cleanup script - Deletes all Offline records.

import requests
import json

#Global Variables
phpipamhost   = "FQDN of PHPipam host"                  #PHPIpam Host
app           = "PHPipam app name"                      #PHPmyipam API App Name
app_token     = "PHPipam app token"                     #PHPmyipam API App Token
token         = ""
Authorization = "Basic auth for PHPipam"                #Username and Pass for PHPipam. Can be generated here https://www.blitter.se/utils/basic-authentication-header-generator/    

#Get token
def get_token():
    global token   
    url = "http://"+phpipamhost+"/api/"+app+"/user"
    payload  = {}
    headers = {
      'Content-Type': 'application/json',
      'token': ''+app_token+'',
      'Authorization': ''+Authorization+'',
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    #Get response as json
    data = response.json()
    #Set token Variable
    token = (data['data']['token'])
  
#Cleanup
def cleanup():
    #Get all Registered ID's
    url = "http://"+phpipamhost+"/api/"+app+"/addresses/"
    payload = "{}"
    headers = {
     'Content-Type': 'application/json',
     'token': ''+token+'',
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    
    #Convert response to json
    json_data = json.loads(response.text)

    #Run thru each item in data
    items = ""
    for item in json_data["data"]:
      id = (item['id'])
      #Check id status
      url = "http://"+phpipamhost+"/api/"+app+"/addresses/"+id+"/ping"
      response = requests.request("GET", url, headers=headers, data = payload)
      #Convert response to json
      result_data = json.loads(response.text)
      result = str(result_data['data']['result_code'])
      if result == "OFFLINE" :
        print (id +" Is offline - Deleting")
        url = "http://"+phpipamhost+"/api/"+app+"/addresses/"+id+""
        response = requests.request("DELETE", url, headers=headers, data = payload)
      else:
        print (id+" Is online - Skipping")

#Run Cleanup
get_token()
cleanup()