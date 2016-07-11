from . import ErrorCode

class ParamInfo:
    def __init__(self,name,default = None):
        self._name      = name
        self._text      = None
        self._value     = None
        self._default   = default
        self._given     = False
        self._errorCode = 0
        self._errorText = ''

    def parse(self,text):
        return self

    def find(self,values):
        return self.parse(values.get(self._name))

    def setError(self,code,*args):
        self._errorCode = code
        self._errorText = ErrorCode.format(self._errorCode,*args)
        return self

    def setValue(self,value):
        self._text = value
        if self._text != None:
            self._value = self._text
            self._given = True
            return True
        self._given = False
        if self._default != None:
            self._value = self._default
            return True
        self.setError( ErrorCode.id_require ,self._name )
        return False


    @property
    def name(self):
        return self._name
    @property
    def text(self):
        return self._text
    @property
    def value(self):
        return self._value
    @property
    def default(self):
        return self._default
    @property
    def given(self):
        return self._given
    @property
    def valid(self):
        return self._errorCode == ErrorCode.id_ok
    @property
    def errorCode(self):
        return self._errorCode
    @property
    def errorText(self):
        return self._errorText
