from .TestCase import TestCase

from param_info import ParamBool
from param_info import Errors

class Test_ParamBool(TestCase):
    def test_require(self):
        self.assertParse( ParamBool('size').parse(    ) , None , Errors.Error_Require , 'size is required' )
    def test_default(self):
        self.assertValid( ParamBool('size',False).parse(       ) , False )
        self.assertValid( ParamBool('size',True ).parse(       ) , True  )
    def test_false(self):
        self.assertValid( ParamBool('size'      ).parse('0'    ) , False )
        self.assertValid( ParamBool('size'      ).parse('off'  ) , False )
        self.assertValid( ParamBool('size'      ).parse('false') , False )
    def test_true(self):
        self.assertValid( ParamBool('size'      ).parse('1'    ) , True  )
        self.assertValid( ParamBool('size'      ).parse('on'   ) , True  )
        self.assertValid( ParamBool('size'      ).parse('true' ) , True  )
    def test_invalid(self):
        self.assertParse( ParamBool('size'      ).parse('dd'   ) , None  , Errors.Error_Bool    , "size=dd should be boolean value : 1,on,true,0,off,false")

if __name__ == '__main__':
    unittest.main()
