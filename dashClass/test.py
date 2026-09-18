from pathlib import Path
from datetime import datetime

tf = Path("data/timestamp.txt")

if tf.is_file():
    with open("data/timestamp.txt", "r") as f:
        ts = f.read()
else:
    with open('data/timestamp.txt', "w") as f:
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S"))