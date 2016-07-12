import unittest
class TestCase(unittest.TestCase):
    def assertParse(self, param, value, error, text):
        self.assertEqual(param.value     , value)
        self.assertEqual(param.errorText , text )
        self.assertTrue ( isinstance(param.error,error) )
    def assertValid(self,param,value):
        self.assertEqual(param.value     , value)
        self.assertEqual(param.error     , None )
        self.assertEqual(param.errorText , ''   )
