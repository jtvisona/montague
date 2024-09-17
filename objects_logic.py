from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Variable:
    __uuid : str = ""
    __symbol : str = ""
    __name : str = "default variable"
    __val : object = field( default_factory=object )
    __str_delim : str = "`"

    def __init__ ( self, symbol = "", name = "" ):
        self.__uuid == self.setUuid()
        if not symbol == "":
            self.__symbol = symbol
        if not name == "":
            self.__name = name

    def getUuid( self ):
        return self.__uuid
    def setUuid( self ):
        self.__uuid = uuid4()

    def getSymbol( self ):
        return self.__symbol
    def setsymbol( self, __symbol ):
        self.__symbol = __symbol

    def getVal( self ):
        return self.__val
    def setVal( self, __val ):
        self.__val = __val

    def getName( self ):
        return self.__name
    def setName( self, __name ):
        self.__name = __name

    def toString( self ): # Cannot put ANYTHING after backslash in these explict continuations
        return f"uuid={self.__uuid} " \
            f"symbol={self.__symbol} " \
            f"name={self.__str_delim}{self.__name}{self.__str_delim} " \
            f"val={self.__val}"
