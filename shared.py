import time

class Shared:
    __encoding = "utf8"
    
    @staticmethod
    def Encoding() -> str:
        return Shared.__encoding
    
    @staticmethod
    def EpochTimestamp() -> int:
        return int(time.time())
    
    @staticmethod
    def Defined(param) -> bool:
        if param: return True
        elif param == True or param == False: return True
        else: return False