  GNU nano 7.1                                           NVD.py                                                     
import requests

API_KEY = "d36bd822-65c8-45cc-b4e1-e95c8ac2da1e"

def get_high_severity_cves():
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    query_params = {
        "cvssV2Severity": "HIGH",
        "api_key": 'd36bd822-65c8-45cc-b4e1-e95c8ac2da1e'
    }
    
    response = requests.get(base_url, params=query_params)
    if response.status_code == 200:
        data = response.json()
        cves = data.get("result", {}).get("CVE_Items", [])
        for cve in cves:
            cve_id = cve.get("cve", {}).get("CVE_data_meta", {}).get("ID")
            cvss_v2_score = cve.get("impact", {}).get("baseMetricV2", {}).get("cvssV2", {}).get("baseScore")
            print(f"CVE ID: {cve_id}")
            print(f"CVSSv2 Score: {cvss_v2_score}")
            print("-----------------------------")
    else:
        print(f"Error: {response.status_code} - {response.text}")

get_high_severity_cves()



