import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime
import webbrowser
import tempfile
import textwrap
load_dotenv()
API_KEY = os.getenv("API_KEY_AVIATION")

if API_KEY is None:
    raise ValueError("API key not set. Please set the AVIATIONSTACK_API_KEY environment variable.")
BASE_URL = os.getenv("BASE_URL")
if BASE_URL is None:
    raise ValueError("Base URL not set. Please set the AVIATIONSTACK_BASE_URL environment variable.")   


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        json_string = json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents)
        sorted_json = sorted(json_string,keys=lambda x: x['flight_date'])
        return json_string
    else:
        json_string = json.dumps(json_thing, sort_keys=sort, indent=indents)
        return json_string

def readFromFile():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def getFlightDataFromFile():
    data = readFromFile()
    if data:
        return pp_json(data)
    else:
        print("Error: No data found in file.")
        return None


def getFlightData(dep_iata, arr_iata):
    url = f"{BASE_URL}flights?access_key={API_KEY}&dep_iata={dep_iata}&arr_iata={arr_iata}"
    #print(f"The actual URL is:{url}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pp_json(data)
       
    else:
        print(f"Error: {response.status_code}")
        return None
    

#Parse the JSON data
def parse_json(json_data):
    outputs = []
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    if 'data' in json_data:
        flights = json_data['data']
        for flight in flights:
            if 'flight' in flight:
                flight_number = flight['flight']['iata']
                
                

            if flight['departure']['estimated']:
                departure_estimated =datetime.fromisoformat(flight['departure']['estimated']).strftime("%B %d, %Y at %I:%M %p %Z")
            else:
                departure_estimated = "Not available"
            if flight['arrival']['estimated']:
                arrival_estimated = datetime.fromisoformat(flight['arrival']['estimated']).strftime("%B %d, %Y at %I:%M %p %Z")
            else:
                arrival_estimated = "Not available"
            

            if flight['departure']['actual_runway']:
                departure_actual = datetime.fromisoformat(flight['departure']['actual_runway']).strftime("%I:%M %p")
            else:
                if flight['departure']['estimated']:
                  departure_actual =datetime.fromisoformat(flight['departure']['estimated']).strftime("%I:%M %p")
                else:
                  departure_actual = "Not available"


            if flight['arrival']['actual_runway']:
                arrival_actual = datetime.fromisoformat(flight['arrival']['actual_runway']).strftime("%I:%M %p")
            else:
                if flight['arrival']['estimated']:
                    arrival_actual = datetime.fromisoformat(flight['arrival']['estimated']).strftime("%I:%M %p")
                else:
                    arrival_actual = "Not available"
            
            if flight['arrival']['terminal']:
                departure_terminal = flight['arrival']['terminal']
            else:
                departure_terminal = "Not available"
            if flight['arrival']['baggage']:
                departure_baggage = flight['arrival']['baggage']
            else:
                departure_baggage = "Not available"

           
            #To upper
            
            #Create a custom json object
            flight = {
                "Flight": flight_number,
                "Date": flight['flight_date'],
                "Status": flight['flight_status'].upper(),
                "Departure": departure_actual,
                "Arrival": arrival_actual,
                "Terminal": departure_terminal
                }
            outputs.append(flight)
        return(outputs)
            
    
    

            

    else:
        print("No flight data found.")


#url = "https://api.aviationstack.com/v1/flights?access_key=c95d7f8ed7d719600805f8e1cea6663b&&dep_iata=CCU&arr_iata=DXB"
#response = requests.get(url)
#pp_json(response.json())






#Definae main function
def main():
    # Get flight data from API
    dep_iata = "CCU"
    arr_iata = "DXB"

     # Get flight data from file
    #flight_data_from_file = getFlightDataFromFile()
    #if flight_data_from_file:
    #    extracted_flights  = parse_json(flight_data_from_file)
    #    extracted_flights = json.dumps(extracted_flights, indent=4)
    #    return extracted_flights


    flight_data = getFlightData(dep_iata, arr_iata) 
    if flight_data:
        extracted_flights  = parse_json(flight_data)
        extracted_flights = json.dumps(extracted_flights, indent=4)
        print("I am going outside now....")
        return extracted_flights
    
    

# Call the main function
if __name__ == "__main__":
    main()
