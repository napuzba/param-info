from .TestCase import TestCase

from param_info import ParamList
from param_info import ParamInfoVal
from param_info import ParamInfoInt
from param_info import ParamInfoStr

from param_info import ErrorCode

class Test_ParamList(TestCase):
    def test_list_01(self):
        params = self.assertValues({},False)
        self.assertError(params,'a1', ErrorCode.id_require,'a1 is required')
        self.assertValue(params,'a2', 7)
        self.assertError(params,'a3', ErrorCode.id_require,'a3 is required')
        self.assertValue(params,'a4', 'cc')
        self.assertValue(params,'a5', 'aa')

    def test_list_02(self):
        params = self.assertValues({'a1':5,'a3':'bb'},True)
        self.assertValue(params,'a1', 5)
        self.assertValue(params,'a2', 7)
        self.assertValue(params,'a3', 'bb')
        self.assertValue(params,'a4', 'cc')
        self.assertValue(params,'a5', 'aa')

    def test_list_03(self):
        params = self.assertValues({'a1':9,'a3':'bb','a4':'abc','a5':'abc'},False)
        self.assertError(params,'a1', ErrorCode.id_intRange ,'a1=9 should be integer in range 5-7')
        self.assertValue(params,'a2', 7)
        self.assertValue(params,'a3', 'bb')
        self.assertError(params,'a4', ErrorCode.id_valFail ,"a4=abc should be one of ['aa', 'bb', 'cc']")
        self.assertValue(params,'a5', 'abc')

    def assertValues(self,values,valid):
        params = ParamList()
        params.add( ParamInfoInt("a1",min=5,max=7) )
        params.add( ParamInfoInt("a2",7,min=5) )
        params.add( ParamInfoVal("a3",['aa','bb','cc']) )
        params.add( ParamInfoVal("a4",['aa','bb','cc'],2) )
        params.add( ParamInfoStr("a5",'aa') )
        self.assertEqual( params.validate(values) , valid)
        return params

    def assertValue(self,params,name,value):
        self.assertEqual(params.errors.get(name),None)
        self.assertEqual(params.params.get(name).value , value)
    def assertError(self,params,name,code,text):
        self.assertEqual(params.errors[name].errorCode,code)
        self.assertEqual(params.errors[name].errorText,text)



if __name__ == '__main__':
    unittest.main()
