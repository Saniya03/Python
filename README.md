# Python
XFEAPI.py function notes

requests IP reputation information from the IBM X-Force API for a specific IP address (IPaddress). The API provides details about the reputation of the given IP address based on various factors, such as past activities, known malicious behavior, and association with security threats.

imports several necessary modules: json, urllib.request, getopt, sys, base64, and time.

sets some global variables, including the base_url for the IBM X-Force API and the standard_header for API requests.
 enters an infinite loop and calls the main() function every hour (3600 seconds) using time.sleep()

 

 NVD.py Creation Notes

uses the requests library to interact with the National Vulnerability Database (NVD) API and retrieve information about high severity Common Vulnerabilities and Exposures (CVEs)
Imports the requests library.
Defines the API key as a constant variable (API_KEY).
Defines the function get_high_severity_cves() that fetches high severity CVEs from the NVD API.
Constructs the base URL for the NVD API , defines query parameters to filter CVEs with a "HIGH" CVSSv2 severity score and includes the API key for authentication.
Sends an HTTP GET request to the NVD API using the requests.get() method, passing the constructed URL and query parameters.
Checks if the response status code is 200 (which indicates a successful request).
If the request is successful, it parses the response JSON data and extracts information about CVEs, including their IDs and CVSSv2 scores.
Prints the CVE ID and CVSSv2 score for each high severity CVE found in the response.
If there is an error in the request (e.g., non-200 status code), it prints the error message.
