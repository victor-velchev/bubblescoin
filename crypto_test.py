import unittest
import hashlib
from shared import Shared
from crypto import Crypto

class TestCrypto(unittest.TestCase):
    def setUp(self):
        #self.whatever
        pass

    def tearDown(self):
         #self.whatever.dispose()
         pass

    def test_sha256(self):
        param = "abcde12345ABCDE67890"
        param_hash_crypto = Crypto.sha256(param)
        param_hash_hashlib = hashlib.sha256(param.encode(Shared.Encoding())).hexdigest()
        self.assertEqual(param_hash_crypto, param_hash_hashlib)

if __name__ == '__main__':
    unittest.main()