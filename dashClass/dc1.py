from datetime import datetime
from nws_json_dash import nws_dash
from test import format_nws_dash

class dashAst(object):
    nextId = 0
    def __init__(self, name=None):
        self.name = name
        self.id = dashAst.nextId
        dashAst.nextId += 1

    def __str__(self):
        now = datetime.now()
        return f"The current time is {now.strftime("%Y-%m-%d %H:%M:%S")}"

    def nws(self):
        print(format_nws_dash())

d1 = dashAst("beacon assistant")
print(d1)
d1.nws()