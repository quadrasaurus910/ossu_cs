import json
import requests
import sys
import dateutil.parser
import dateutil.tz


def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]


def format_utc_to_eastern(utc_timestamp_str):
    target_tz = dateutil.tz.gettz('US/Eastern')
    eastern_dt = dateutil.parser.parse(utc_timestamp_str).astimezone(target_tz)
    day = eastern_dt.day
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th') if not 10 <= day % 100 <= 20 else 'th'
    return eastern_dt.strftime(f"%B {day}{suffix}, %I:%M %p").replace(" 0", " ")


def nws_to_json(response, keys):
    json_response = response.json()
    nws_properties = json_response["properties"]
    list_of_properties = []
    dp = {}
    for key, value_data in properties.items():
        if key in keys:
            property_name = key
            display_value = None
            unit = ""

            # Check for dictionary values
            if isinstance(value_data, dict):
                actual_value = value_data.get("value") # Use .get() for safer access
                list_of_properties.append({"name": property_name, "value": actual_value})
                dp[property_name] = actual_value
            else:
                if value_data is not None:
                    # Check if the value is an empty list, and if so, skip it
                    if isinstance(value_data, list) and not value_data:
                        continue
                    if isinstance(value_data, (int, float)):
                        display_value = value_data
                    else:
                        display_value = str(value_data)
                    list_of_properties.append({"name": property_name, "value": display_value})
                    dp[property_name] = display_value
    for i in list_of_properties:
        if i["value"] != None:
            if i["name"] == "windDirection":
                i["value"] = degToCompass(int(i["value"]))
            if i["name"] in ["windSpeed", "windGust"]:
                converted_wind = round((i['value'] * 0.621371), 2)
                i["value"] = f"{converted_wind} MPH"
            if i["name"] == "timestamp":
                i["value"] = format_utc_to_eastern(i["value"])
            if i["name"] == "temperature":
                i["value"] = ((i["value"] * 9/5) + 32)
            #print(f"{i['name']} : {i['value']}")
    for key, value in dp.items():
        ...
        #print(f"{key}: {value}")
    #print(dp)


response = requests.get("https://api.weather.gov/stations/KSUT/observations/latest?require_qc=false")
response.raise_for_status()
keys = ["stationName",
        "timestamp",
        "textDescription",
        "temperature",
        "windChill",
        "heatIndex",
        "windDirection",
        "windSpeed",
        "relativeHumidity",
        ]
j = response.json()
properties = j["properties"]
pretty_json = json.dumps(j, indent=4)
#print(pretty_json)
nws_to_json(response, keys)

propDict = {}
propList = []
for i in properties:
    listDict = {}
    if i == "timestamp":
        properties[i] = format_utc_to_eastern(properties[i])
    if type(properties[i]) is str:
        propDict[i] = properties[i]
        listDict["name"] = str(i)
        listDict["value"] = properties[i]
        propList.append(listDict)
    elif type(properties[i]) is dict:
        #print(properties[i])
        listDict["name"] = str(i)
        listDict["value"] = properties[i]["value"]
        listDict["wmoUnit"] = properties[i]["unitCode"].split(":")[1]
        propList.append(listDict)
        propDict[i] = properties[i]["value"]
#print(propDict)
for i in propList:
    if i["value"] != None and i["name"] in keys:
        if i.get("wmoUnit", "none") == "degC":
            i["value"] = ((i["value"] * 9/5) + 32)
            i["wmoUnit"] = "°F"
        if i["name"] == "windDirection":
            ...
            #i["value"] = degToCompass(int(i["value"]))
        if i["name"] in ["windSpeed", "windGust"]:
            converted_wind = round((i['value'] * 0.621371), 2)
            i["value"] = f"{converted_wind} MPH {degToCompass(int(i["value"]))}"
            i["wmoUnit"] = ""
        if type(i["value"]) is float:
            i["value"] = round(i["value"], 2)
        if i.get("wmoUnit", "none") == "percent":
            i["wmoUnit"] = "%"
        # print(f"{i['name']}: {i['value']} {i.get('wmoUnit', '')}")

def nws_dash():
    keys = ["stationName",
        "timestamp",
        "textDescription",
        "temperature",
        "windChill",
        "heatIndex",
        "windDirection",
        "windSpeed",
        "relativeHumidity",
        ]
    return keys

