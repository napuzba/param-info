from .TestCase import TestCase

from param_info import ParamInfoVal
from param_info import ErrorCode

class Test_ParamInfoVal(TestCase):
    def test_require(self):
        self.assertParse( ParamInfoVal('size',['aa','bb','cc']).parse()   , None , ErrorCode.id_require    , 'size is required' )
    def test_valid(self):
        self.assertParse( ParamInfoVal('size',['aa','bb','cc'],1).parse()      , "bb"    , ErrorCode.id_ok       , '')
        self.assertParse( ParamInfoVal('size',['aa','bb','cc'],2).parse('aa')  , "aa"    , ErrorCode.id_ok       , '')
    def test_invalid(self):
        self.assertParse( ParamInfoVal('size',['aa','bb','cc'],2).parse('dd')  , "dd"    , ErrorCode.id_valFail , "size=dd should be one of ['aa', 'bb', 'cc']")

if __name__ == '__main__':
    unittest.main()
