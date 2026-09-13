from datetime import datetime

class dashAst(object):
    nextId = 0
    def __init__(self, name=None):
        self.name = name
        self.id = dashAst.nextId
        dashAst.nextId += 1

    def __str__(self):
        now = datetime.now()
        return f"The current time is {now.strftime("%Y-%m-%d %H:%M:%S")}"

d1 = dashAst("beacon assistant")
print(d1)