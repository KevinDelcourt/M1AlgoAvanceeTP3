import datetime


class Log:
    def __init__(self):
        self.log = str(datetime.datetime.now()) + "\n"

    def time(self):
        self.log += "\n" + str(datetime.datetime.now()) + "\n"

    def write(self, stuff, tabs=0):
        tabstr = ""
        for _ in range(0, tabs):
            tabstr += "\t"
        self.log += tabstr+str(stuff)+"\n"

    def __del__(self):
        self.time()
        file = open("./logs/"+str(datetime.datetime.now()), 'w')
        file.write(self.log)
