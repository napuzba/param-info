from .TestCase import TestCase

from param_info import ParamInfoVal
from param_info import Errors

class Test_ParamInfoVal(TestCase):
    def test_require(self):
        self.assertParse( ParamInfoVal('size',['aa','bb','cc']  ).parse(    ) , None , Errors.Error_Require , 'size is required' )
    def test_valid(self):
        self.assertValid( ParamInfoVal('size',['aa','bb','cc'],1).parse(    ) , "bb" )
        self.assertValid( ParamInfoVal('size',['aa','bb','cc'],2).parse('aa') , "aa" )
    def test_invalid(self):
        self.assertParse( ParamInfoVal('size',['aa','bb','cc'],2).parse('dd') , None , Errors.Error_Val    , "size=dd should be one of aa,bb,cc")

if __name__ == '__main__':
    unittest.main()
