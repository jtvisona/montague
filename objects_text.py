from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Proposition:
    __uuid : str = ""
    __prop : str = "There is no assigned proposition."
    __lang : str = "english"
    __str_delim : str = "`"

    def __init__ ( self, prop = "", lang = "" ):
        self.__uuid == self.setUuid()
        if not prop == "":
            self.__prop = prop
        if not lang == "":
            self.__lang = lang

    def getUuid( self ):
        return self.__uuid
    def setUuid( self ):
        self.__uuid = uuid4()

    def getProp( self ):
        return self.__prop
    def setProp( self, prop ):
        self.__prop = prop

    def toString( self ): # Cannot put ANYTHING after backslash in these explict continuations
        return f"uuid={self.__uuid} " \
            f"prop={self.__str_delim}{self.__prop}{self.__str_delim} " \
            f"lang={self.__lang}"