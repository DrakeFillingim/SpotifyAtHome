import time

class Timer:
    def __init__(self, onTimeout):
        self.startTime = None
        self.endTime = None


    def Tick(self):
        pass

    def Start(self, runTime):
        self.startTime = time.time()
        

    def Reset(self):
        pass
