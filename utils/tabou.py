import math


class Tabou:
    def __init__(self, k=math.inf):
        self.k = k
        self.list = []

    def push_obj(self, obj):
        self.list.append(obj)
        if len(self.list) > self.k:
            self.list.pop(0)

    def __repr__(self):
        return str(self.list)
