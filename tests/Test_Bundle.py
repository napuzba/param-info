from .TestCase import TestCase

from param_info import Bundle
from param_info import ParamVal
from param_info import ParamInt
from param_info import ParamStr
from param_info import Errors

class Test_Bundle(TestCase):
    def test_bundle_01(self):
        params = self.assertValues({},False)
        self.assertError(params,'a1', Errors.Error_Require,'a1 is required')
        self.assertValue(params,'a2', 7)
        self.assertError(params,'a3', Errors.Error_Require,'a3 is required')
        self.assertValue(params,'a4', 'cc')
        self.assertValue(params,'a5', 'aa')

    def test_bundle_02(self):
        params = self.assertValues({'a1':5,'a3':'bb'},True)
        self.assertValue(params,'a1', 5)
        self.assertValue(params,'a2', 7)
        self.assertValue(params,'a3', 'bb')
        self.assertValue(params,'a4', 'cc')
        self.assertValue(params,'a5', 'aa')

    def test_bundle_03(self):
        params = self.assertValues({'a1':9,'a3':'bb','a4':'abc','a5':'abc'},False)
        self.assertError(params,'a1', Errors.Error_IntRange    ,'a1=9 should be integer in range 5-7')
        self.assertValue(params,'a2', 7)
        self.assertValue(params,'a3', 'bb')
        self.assertError(params,'a4', Errors.Error_Val         ,"a4=abc should be one of aa,bb,cc")
        self.assertValue(params,'a5', 'abc')

    def assertValues(self,values,valid):
        params = Bundle()
        params.add( ParamInt("a1",min=5,max=7) )
        params.add( ParamInt("a2",7,min=5) )
        params.add( ParamVal("a3",['aa','bb','cc']) )
        params.add( ParamVal("a4",['aa','bb','cc'],2) )
        params.add( ParamStr("a5",'aa') )
        self.assertEqual( params.validate(values) , valid)
        return params

    def assertValue(self,params,name,value):
        self.assertEqual(params.errors.get(name),None)
        self.assertEqual(params.params.get(name).value , value)
    def assertError(self,params,name,error,text):
        self.assertTrue (isinstance(params.errors[name].error , error))
        self.assertEqual(params.errors[name].errorText,text)

if __name__ == '__main__':
    unittest.main()
