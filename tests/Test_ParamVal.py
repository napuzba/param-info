from .TestCase import TestCase

from param_info import ParamVal
from param_info import Errors

class Test_ParamVal(TestCase):
    def test_require(self):
        self.assertParse( ParamVal('size',['aa','bb','cc']  ).parse(    ) , None , Errors.Error_Require , 'size is required' )
    def test_valid(self):
        self.assertValid( ParamVal('size',['aa','bb','cc'],1).parse(    ) , "bb" )
        self.assertValid( ParamVal('size',['aa','bb','cc'],2).parse('aa') , "aa" )
    def test_invalid(self):
        self.assertParse( ParamVal('size',['aa','bb','cc'],2).parse('dd') , None , Errors.Error_Val    , "size=dd should be one of aa,bb,cc")

if __name__ == '__main__':
    unittest.main()
