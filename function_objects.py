from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Process:
    __uuid : str = ""
    __name : str = "default process"
    __args : dict = field( default_factory=dict ) ## Note the use of a field
    __str_delim : str = "`"

    def __init__ ( self, name = "", args = {} ):
        self.__uuid == self.setUuid()
        if not name == "":
            self.__prop = name
            self.__args = args

    def getUuid( self ):
        return self.__uuid
    def setUuid( self ):
        self.__uuid = uuid4()

    def getName( self ):
        return self.__name
    def setName( self, name ):
        self.__name = name

    def getArgs( self ):
        return self.__args
    def setArgs( self, args ):
        self.__args = args

    def toString( self ):
        return f"uuid={self.__uuid} " \
            f"name={self.__str_delim}{self.__name}{self.__str_delim} " \
            f"args={self.__args} "
    