from pathlib import Path
from datetime import datetime
from nws_json_dash import nws_dash
import json

tf = Path("data/timestamp.csv")
ts = None

if tf.is_file():
    with open("data/timestamp.csv", "r") as f:
        ts = f.read()
        d1 = datetime.now() - datetime.fromisoformat(ts)
        if ts != None:
            try:
                tsi = datetime.fromisoformat(ts)
                td1 = int((datetime.now() - datetime.fromisoformat(ts)).total_seconds() // 60)
                if td1 < 5:
                    ...
                else:
                    ...
            except:
                print("error")
else:
    with open('data/timestamp.csv', "w") as f:
        now = datetime.now().isoformat()
        f.write(now)
        #f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

# print(datetime.now().isoformat())


def timeCheck():
    timeFile = Path("data/timestamp.csv")
    timestamp = None
    if timeFile.is_file():
        with open("data/timestamp.csv", "r") as f:
            timestamp = f.read()
            if timestamp != None:
                try:
                    timedelta = int((datetime.now() - datetime.fromisoformat(ts)).total_seconds() // 60)
                    if timedelta < 5:
                        return False
                    else:
                        return True
                except:
                    return False


def get_nws_json():
    if timeCheck() == False:
        print('timeCheck is false')
        with open('data/nws.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        print('timeCheck is true')
        nwsDash = nws_dash()
        with open("data/nws.json", "w") as file:
            json.dump(nwsDash, file, indent=4)
        with open('data/timestamp.csv', "w") as f:
            f.write(datetime.now().isoformat())
        


def format_nws_dash():
    """Returns str of NWS json data formatted for dashClass"""
    with open('data/nws.json', 'r', encoding='utf-8') as file:
        nws_json = json.load(file)
        for i in nws_json:
            print(i)

print(format_nws_dash())