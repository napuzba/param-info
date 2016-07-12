from .TestCase import TestCase
from param_info import ParamInfoStr
from param_info import Errors

class Test_ParamInfoStr(TestCase):
    def test_require(self):
        self.assertParse( ParamInfoStr('size'    ).parse()            , None    , Errors.Error_Require , 'size is required' )
        self.assertValid( ParamInfoStr('size',"5").parse()            , "5"     )
    def test_any(self):
        self.assertValid( ParamInfoStr('size'    ).parse("  hallo  ") , "hallo" )

if __name__ == '__main__':
    unittest.main()
