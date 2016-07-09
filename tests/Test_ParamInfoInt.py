from .TestCase import TestCase
from param_info import ParamInfoInt
from param_info import ErrorCode

class Test_ParamInfoInt(TestCase):
    def test_require(self):
        self.assertParse( ParamInfoInt('size').parse()   , None , ErrorCode.id_require    , 'size is required' )
        self.assertParse( ParamInfoInt('size',5).parse() , 5    , ErrorCode.id_ok         , '')

    def test_anyInt(self):
        self.assertParse( ParamInfoInt('size').parse("5")  , 5    , ErrorCode.id_ok       , '')
        self.assertParse( ParamInfoInt('size').parse("aa") , None , ErrorCode.id_int      , 'size=aa should be integer')

    def test_min(self):
        self.assertParse( ParamInfoInt('size',min=5).parse("6") , 6 , ErrorCode.id_ok     , '')
        self.assertParse( ParamInfoInt('size',min=5).parse("4") , 4 , ErrorCode.id_intMin , 'size=4 should be integer >= 5')

    def test_max(self):
        self.assertParse( ParamInfoInt('size',max=5).parse("4") , 4 , ErrorCode.id_ok     , '')
        self.assertParse( ParamInfoInt('size',max=5).parse("6") , 6 , ErrorCode.id_intMax , 'size=6 should be integer <= 5')


    def test_range(self):
        self.assertParse( ParamInfoInt('size',min=4,max=6).parse("5") , 5 , ErrorCode.id_ok       , '')
        self.assertParse( ParamInfoInt('size',min=2,max=4).parse("5") , 5 , ErrorCode.id_intRange , 'size=5 should be integer in range 2-4')
        self.assertParse( ParamInfoInt('size',min=6,max=8).parse("5") , 5 , ErrorCode.id_intRange , 'size=5 should be integer in range 6-8')

if __name__ == '__main__':
    unittest.main()
