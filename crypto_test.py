from crypto import Crypto
import hashlib
from shared import Shared
import unittest


class TestCrypto(unittest.TestCase):
    def setUp(self):
        # self.whatever
        pass

    def tearDown(self):
        # self.whatever.dispose()
        pass

    def test_sha256(self):
        param = "abcde12345ABCDE67890"
        param = param.encode(Shared.Encoding())
        param_hash_crypto = Crypto.sha256(param)
        param_hash_hashlib = hashlib.sha256(param).hexdigest()
        self.assertEqual(param_hash_crypto, param_hash_hashlib)

if __name__ is '__main__':
    unittest.main()
