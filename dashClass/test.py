from pathlib import Path
from datetime import datetime

tf = Path("data/timestamp.csv")
ts = None

if tf.is_file():
    with open("data/timestamp.csv", "r") as f:
        ts = f.read()
        print(ts)
        if ts != None:
            try:
                print(datetime.now().isoformat() - datetime.fromisoformat(ts))
            except:
                print("error")
else:
    with open('data/timestamp.csv', "w") as f:
        now = datetime.now().isoformat()
        f.write(now)
        #f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

# print(datetime.now().isoformat())