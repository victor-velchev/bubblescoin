from shared import Shared
import unittest


class TestShared(unittest.TestCase):
    def setUp(self):
        # self.whatever
        pass

    def tearDown(self):
        # self.whatever.dispose()
        pass

    def test_encoding(self):
        self.assertTrue(isinstance(Shared.Encoding(), str))
        self.assertEqual(Shared.Encoding(), "utf8")

    def test_epoch_timestamp(self):
        self.assertTrue(isinstance(Shared.EpochTimestamp(), int))
        self.assertTrue(Shared.EpochTimestamp() > 0)

    def test_defined_string(self):
        param_string = "house"
        self.assertTrue(Shared.Defined(param_string))
        param_string = ""
        self.assertFalse(Shared.Defined(param_string))

    def test_defined_int(self):
        param_int = 6
        self.assertTrue(Shared.Defined(param_int))
        param_int = -6
        self.assertTrue(Shared.Defined(param_int))
        param_int = 0
        self.assertTrue(Shared.Defined(param_int))

    def test_defined_float(self):
        param_float = 6.5
        self.assertTrue(Shared.Defined(param_float))
        param_float = -6.5
        self.assertTrue(Shared.Defined(param_float))
        param_float = 0
        self.assertTrue(Shared.Defined(param_float))

    def test_defined_list(self):
        param_list = ["house", 6, 6.5]
        self.assertTrue(Shared.Defined(param_list))
        param_list = []
        self.assertFalse(Shared.Defined(param_list))

    def test_defined_dict(self):
        param_dict = {"foo": "bar"}
        self.assertTrue(Shared.Defined(param_dict))
        param_dict = {}
        self.assertFalse(Shared.Defined(param_dict))

    def test_defined_bool(self):
        param_bool = True
        self.assertTrue(Shared.Defined(param_bool))
        param_bool = False
        self.assertTrue(Shared.Defined(param_bool))

if __name__ is '__main__':
    unittest.main()
