from .TestCase import TestCase
from param_info import ParamInfoStr
from param_info import ErrorCode

class Test_ParamInfoStr(TestCase):
    def test_require(self):
        self.assertParse( ParamInfoStr('size').parse()     , None , ErrorCode.id_require      , 'size is required' )
        self.assertParse( ParamInfoStr('size',"5").parse() , "5"    , ErrorCode.id_ok         , '')
    def test_any(self):
        self.assertParse( ParamInfoStr('size').parse("  hallo  ")  , "hallo"    , ErrorCode.id_ok         , '')

if __name__ == '__main__':
    unittest.main()
