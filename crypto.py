import hashlib
from shared import Shared


class Crypto(object):
    # returns a string of double length, containing only hexadecimal digits
    @staticmethod
    def sha256(param) -> str:
        if Shared.Defined(param) is False:
            print(__name__, "param was not defined!")
            return False
        hashed_param = hashlib.sha256(param.encode(Shared.Encoding()))
        return hashed_param.hexdigest()
