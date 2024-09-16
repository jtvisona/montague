from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Proposition:
    __uuid : str = ""
    __prop : str = "There is no assigned proposition."
    __str_delim : str = "`"

    def __init__ ( self, prop = "" ):
        self.__uuid == self.setUuid()
        if not prop == "":
            self.__prop = prop

    def getUuid( self ):
        return self.__uuid
    def setUuid( self ):
        self.__uuid = uuid4()

    def getProp( self ):
        return self.__prop
    def setProp( self, prop ):
        self.__prop = prop

    def toString( self ):
        return f"uuid={self.__uuid} prop={self.__str_delim}{self.__prop}`{self.__str_delim}"