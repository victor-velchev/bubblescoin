import time

class Shared:
    __encoding = "utf8"
    
    @staticmethod
    def Encoding():
        return Shared.__encoding
    
    def EpochTimestamp():
        return int(time.time())
    
    def Defined(param) -> bool:
        if param: return True
        elif param == True or param == False: return True
        else: return False