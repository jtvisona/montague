from dataclasses import dataclass, field
from objects_base import Object

@dataclass
class Set( Object ):
    __uuid : str = ""
    ##__type another way to indicate type of class?
    __name : str = "default Set"
    __val : set = field( default_factory=set ) # consider using __value for all objects
    __type : str = ""

    def __init__ ( self, val = {}, type = "" ):
        self.__uuid == self.setUuid()
        if not val == {}:
            self.__val = val
        if not type == "":
            self.__type = type

    def getUuid( self ):
        return self.__uuid
    def setUuid( self ):
        self.__uuid = uuid4()

    def getSet( self ):
        return self.__val
    def setSet( self, val ):
        self.__val = val

    def toString( self ):
        return f"uuid={self.__uuid} " \
            f"val={self.__val} " \
            f"type={self.__type}"