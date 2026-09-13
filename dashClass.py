from datetime import datetime

class dashAst(object):
    nextId = 0
    def __init__(self, name=None):
        self.name = name
        self.id = nextId
        nextId += 1

    def str(self):
        now = datetime.now()
        return now

d1 = dashAst("beacon assistant")
print(d1)