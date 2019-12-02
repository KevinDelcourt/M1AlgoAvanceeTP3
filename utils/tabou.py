import math


class Tabou:
    def __init__(self, k=math.inf, verbose=False):
        self.k = k
        self.verbose = verbose
        self.list = []
        if self.verbose:
            print("\033[0;34mTabou : ", end="")
            print(self.list, end="")
            print("\033[0m")

    def push_obj(self, obj):
        self.list.append(obj)
        if len(self.list) > self.k:
            self.list.pop(0)
        if self.verbose:
            print("\033[0;34mTabou : ", end="")
            print(self.list, end="")
            print("\033[0m")
