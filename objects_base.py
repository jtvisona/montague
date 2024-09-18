import globals as G
import utility as U
from dataclasses import dataclass

from uuid import uuid4

# ----------------------------------------------------------------
# OBJECT
# ----------------------------------------------------------------

"""
Base class for all objects contained in the montague application.
"""

@dataclass
class Object:
    __uuid: str = ""
    __type: str = ""
    __name: str = ""
    __delim: str = "`"

    def __init__ ( self, name: str = "" ):
        self.__uuid = uuid4() # returns UUID obj and not string; to convert str(self.__uuid)
        self.__type = type( self )
        if not name == "":
            self.__name = name

    @property
    def uuid( self ):
        return self.__uuid
    @uuid.setter
    def uuid( self, uuid: str ):
        self.__uuid = uuid
    def stringified_uuid( self ):
        return str( self.__uuid )
    def regen_uuid( self ):
        self.__uuid = uuid4()

    @property
    def type( self ):
        return self.__type

    @property
    def name( self ):
        return self.__name
    @name.setter
    def name( self, name: str ):
        self.__name = name

    @property
    def delim( self ):
        return self.__delim
    @delim.setter
    def delim( self, delim: str ):
        self.__delim = delim

    def to_string( self ):
        return f"uuid={self.__uuid} " \
            f"type={self.__type} " \
            f"name={self.__delim}{self.__name}{self.__delim} "
