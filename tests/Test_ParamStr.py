from .TestCase import TestCase
from param_info import ParamStr
from param_info import Errors

class Test_ParamStr(TestCase):
    def test_require(self):
        self.assertParse( ParamStr('size'    ).parse()            , None    , Errors.Error_Require , 'size is required' )
        self.assertValid( ParamStr('size',"5").parse()            , "5"     )
    def test_any(self):
        self.assertValid( ParamStr('size'    ).parse("  hallo  ") , "hallo" )

if __name__ == '__main__':
    unittest.main()
