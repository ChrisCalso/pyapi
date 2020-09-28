#!/usr/bin/python3
import requests

## Define NEOW URL 
#NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"
MARSURL = "https://api.nasa.gov/insight_weather/?"
def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
   # startdate = "start_date=2020-09-27"
    feedtype = "feedtype=json"
    ver  ="ver=1.0"
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
   # neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    neowrequest = requests.get(MARSURL + nasacreds + "&" + feedtype+ "&" + ver)
    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

