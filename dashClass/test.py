from pathlib import Path
from datetime import datetime

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