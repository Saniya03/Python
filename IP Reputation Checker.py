import json
import urllib.request
import getopt
import sys
import base64

############# SECTION 1 ###########################
# Globals
base_url = 'https://api.xforce.ibmcloud.com'
standard_header = {'Accept': 'application/json'}

############# SECTION 2 ###########################
# Credentials
API_Key = 'bd954eef-2ed5-431c-b7fb-60c736fb1728'
API_Pwd = '3bda8ab3-3cf7-4859-bcae-2bb2f0625d5e'

############# SECTION 3 ###########################
### IP reputation request
IPrep_url = '/ipr/history/'
IPaddress = '78.58.230.174'
### CVE request; example CVE-2017-5754
CVE_url = '/vulnerabilities/search/'
CVE_num = 'CVE-2017-5754'

############# SECTION 4 ###########################
##### Create BA Token
def createToken():
    credentials = '{}:{}'.format(API_Key, API_Pwd)
    credentials_bytes = credentials.encode('utf-8')
    base64_bytes = base64.b64encode(credentials_bytes)
    base64_string = base64_bytes.decode('utf-8')
    BA_header = 'Basic ' + base64_string
    return BA_header

############# SECTION 5 ###########################
def main():
    # Create HTTP request
    url = base_url + IPrep_url + IPaddress
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/json')
    req.add_header('Authorization', createToken())

    # Submit the request
    try:
        response = urllib.request.urlopen(req)
        resp_data = response.read()
        resp_data_json = json.loads(resp_data)
        response.close()
        print(json.dumps(resp_data_json, indent=4, sort_keys=True))
    except urllib.error.URLError as e:
        print("-------------------------")
        print("The request has an error")
        print("HTTP " + str(e.code))
        print("Description: " + str(e.reason))
        print("")
        print("Request details are:")
        print("URL: " + url)
        print("")
        print("Headers: ")
        print(str(req.header_items()))
        print("")

############# SECTION 6 ###########################
main()



