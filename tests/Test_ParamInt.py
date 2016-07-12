from .TestCase import TestCase
from param_info import ParamInt
from param_info import Errors

class Test_ParamInt(TestCase):
    def test_require(self):
        self.assertValid( ParamInt('size',5          ).parse(    ) , 5    )
        self.assertParse( ParamInt('size'            ).parse(    ) , None , Errors.Error_Require , 'size is required' )
    def test_anyInt(self):
        self.assertValid( ParamInt('size'            ).parse("5" ) , 5    )
        self.assertParse( ParamInt('size'            ).parse("aa") , None , Errors.Error_Int     , 'size=aa should be integer')
    def test_min(self):
        self.assertValid( ParamInt('size',min=5      ).parse("6" ) , 6    )
        self.assertParse( ParamInt('size',min=5      ).parse("4" ) , 4    , Errors.Error_IntMin  , 'size=4 should be integer >= 5')
    def test_max(self):
        self.assertValid( ParamInt('size',max=5      ).parse("4" ) , 4    )
        self.assertParse( ParamInt('size',max=5      ).parse("6" ) , 6    , Errors.Error_IntMax  , 'size=6 should be integer <= 5')
    def test_range(self):
        self.assertValid( ParamInt('size',min=4,max=6).parse("5" ) , 5    )
        self.assertParse( ParamInt('size',min=2,max=4).parse("5" ) , 5    , Errors.Error_IntRange , 'size=5 should be integer in range 2-4')
        self.assertParse( ParamInt('size',min=6,max=8).parse("5" ) , 5    , Errors.Error_IntRange , 'size=5 should be integer in range 6-8')

if __name__ == '__main__':
    unittest.main()
