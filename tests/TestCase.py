import unittest
class TestCase(unittest.TestCase):
    def assertParse(self, info, value, code, text):
        self.assertEqual(info.value     , value)
        self.assertEqual(info.errorCode , code )
        self.assertEqual(info.errorText , text )
