from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Object:
    __uuid : str = ""
    __type : str = ""
    __name : str = ""
    __str_delim : str = "`"

    def __init__ ( self, name = "" ):
        self.__uuid = self.genUuid()
        self.__type = type( self )
        if not name == "":
            self.__name = name

    @property
    def uuid( self ):
        return self.__uuid
    @uuid.setter
    def uuid( self, uuid ):
        self.__uuid = uuid
    def genUuid( self ):
        self.__uuid = uuid4()

    @property
    def type( self ):
        return self.__type

    @property
    def name( self ):
        return self.__name
    @name.setter
    def name( self, name ):
        self.__name = name

    @property
    def delim( self ):
        return self.__str_delim
    @delim.setter
    def delim( self, delim ):
        self.__str_delim = delim

    def toString( self ):
        return f"uuid={self.__uuid} " \
            f"type={self.__type} " \
            f"name={self.__str_delim}{self.__name}{self.__str_delim} "
    