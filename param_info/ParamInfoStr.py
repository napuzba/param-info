from .ParamInfo import *
from winreg import SetValue

class ParamInfoStr(ParamInfo):
    def __init__(self,name,default = None):
        super().__init__(name,default)

    def parse(self,text=None):
        if not self.setValue(text):
            return self
        self._value = self._value.strip()
        return self.setError( ErrorCode.id_ok ,self._name )
