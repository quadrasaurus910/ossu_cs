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
    response = requests.get("https://api.weather.gov/stations/KSUT/observations/latest?require_qc=false")
    response.raise_for_status()
    j = response.json()
    properties = j["properties"]
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
    return propList
            

